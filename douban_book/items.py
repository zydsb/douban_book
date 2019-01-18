# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  #书名
    link = scrapy.Field()  #链接
    author = scrapy.Field()  #作者
    score = scrapy.Field()  #评分
    scoreNum = scrapy.Field() #评论人数 
    press = scrapy.Field()  #出版社
    isbn = scrapy.Field()  #isbn
    price = scrapy.Field()  #价格
    publishyear = scrapy.Field()  #出版年
    authordesc = scrapy.Field()  #作者简介
    bookdesc = scrapy.Field()  #书简介
    label = scrapy.Field() #标签
    pagecount = scrapy.Field() #字数
    imgUrl = scrapy.Field() #图片链接