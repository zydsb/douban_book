import scrapy
import re
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from douban_book.items import DoubanBookItem

class doubanSpider(scrapy.Spider):
    name = "douban_book"
    allowed_domains = ["douban.com"] #搜索的域名范围，也就是爬虫的约束区域
    start_urls = ['https://book.douban.com/subject/6082808/']

    def parse(self, response):
        
        book = DoubanBookItem()
        if response.status==200:
            try:
                title = response.xpath("//div[@id='wrapper']/h1/span/text()").extract()  
                link = response.url
                imgUrl = response.xpath("//div[@id='mainpic']/a[@class='nbg']/@href").extract_first()
                author = response.xpath("//div[@id='info']/a[1]/text()").extract()
                score = response.xpath("//div[@id='interest_sectl']/div/div[2]/strong/text()").extract()
                score_num = response.xpath("//div[@id='interest_sectl']/div/div[2]/div/div[2]/span/a/span/text()").extract()
                label = response.xpath("//a[@class='  tag']/text()").extract()
                bookdesc = response.xpath("//*[@id='link-report']/div[1]/div/p/text()").extract()
                authordesc = response.xpath("//*[@id='content']/div/div[1]/div[3]/div[2]/div/div/p/text()").extract()
                infos = response.xpath("//div[@id='info']")
                for info in infos.xpath("./*|./text()"):
                    name = info.xpath("text()").extract_first()
                    if name is not None:
                        curType = ""
                    if "出版社:" == name:
                        curType = "press"
                        continue
                    elif "出版年:" == name:
                        curType = "publishyear"
                        continue
                    elif "页数:" == name:
                        curType = "pagecount"
                        continue
                    elif "定价:" == name:
                        curType = "price"
                        continue
                    elif "ISBN:" == name:
                        curType = "isbn"
                        continue

                    span = info.extract()
                    span = span.strip()  # 去掉空格
                    span = span.replace("\n", "")  # 去掉换行符
                    span = span.replace("<br>", "")  # 去掉换行符
                    

                    if len(span) != 0:
                        if curType == "press":
                            book['press'] = span
                        elif curType == "publishyear":
                            book['publishyear'] = span
                        elif curType == "pagecount":
                            book['pagecount'] = int(re.sub("\D", "", span))  #todo 这里限制只获取数字 去掉冒号 单位
                        elif curType == "price":
                            book['price'] = float(re.findall(r"\d+\.?\d*",span)[0])
                        elif curType == "isbn":
                            book['isbn'] = span

                book['title'] = title
                book['link'] = link
                book['imgurl'] = imgurl
                book['author'] = author
                book['score'] = score
                book['label'] = label 
                book['authordesc'] = authordesc
                book['bookdesc'] =  bookdesc
         
                print(book)
                yield book
                
                
                continueurls = response.xpath("//div[@id='db-rec-section']/div[@class='content clearfix']/dl/dt/a/@href").extract()
                 
                for url in continueurls:
                    yield scrapy.Request(url)
                
            except:
                print('-'*30 + 'error' + '-'*30)
        else:
            print('*'*99)
        
