# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewimdbcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_urls= scrapy.Field()
    images = scrapy.Field()
    title = scrapy.Field()
    rating = scrapy.Field()
    directors = scrapy.Field()
    writers = scrapy.Field()
    stars = scrapy.Field()
    popularity = scrapy.Field()
    time = scrapy.Field()
    genre = scrapy.Field()
    description = scrapy.Field()
    releasedate = scrapy.Field()
    totalrating = scrapy.Field()
    company = scrapy.Field() 
    total_cast = scrapy.Field()

