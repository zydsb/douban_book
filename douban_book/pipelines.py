# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql
import re 


class DoubanBookPipeline(object):

    
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root',
                               passwd='45486081A', db='doubanbook', charset='utf8')
        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):
        rep = re.compile('\n| ')
        title = item.get('title','N/A')
        author_tmp = item.get('author','N/A')
        score_tmp = item.get('score',0.0)
        scorenum = item.get('scorenum',0)
        press = item.get('press','N/A')
        isbn = item.get('isbn',0)
        price = item.get('price',0.0)
        publishyear = item.get('publishyear','N/A')
        pagecount = item.get('pagecount',0)
        label_tmp = item.get('label','N/A')

        label = ",".join(label_tmp)
        if score_tmp:
            score = score_tmp[0].strip()
        else:
            score = 0.0
        if author_tmp:
            author = rep.sub('',author_tmp[0])
        else:
            author = 'zhangyang'

        

        sql = "replace into book_info (title,author,press,isbn,price,publishyear,label,pagecount) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        print(sql,(title,author,score,scorenum,press,isbn,price,publishyear,label,pagecount))
        self.cursor.execute(sql,(title,author,press,isbn,price,publishyear,label,pagecount))
        self.conn.commit()


    def close_spider(self, spider):
        self.conn.close()