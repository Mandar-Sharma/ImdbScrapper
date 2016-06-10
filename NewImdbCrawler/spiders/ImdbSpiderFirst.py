# -*- coding: utf-8 -*-
import scrapy
import logging
from NewImdbCrawler.items import NewimdbcrawlerItem

class SecondSpiderSpider(scrapy.Spider):
    name = "imdbspidergo"
    allowed_domains = ["imdb.com"]
    start_urls = (
        'http://www.imdb.com/chart/top',
    )

    def parse(self, response):
        links = response.xpath('//tbody[@class="lister-list"]/tr/td[@class="titleColumn"]/a/@href').extract()
        i =1 
        for link in links:
            abs_url = response.urljoin(link)
            url_next = '//*[@id="main"]/div/span/div/div/div[2]/table/tbody/tr['+str(i)+']/td[3]/strong/text()'
            rating = response.xpath(url_next).extract()
            if (i <= len(links)):
                i=i+1
            yield scrapy.Request(abs_url, callback = self.parse_indetail, meta={'rating' : rating})
        #prev_link=response.xpath('//div[@class="sort"]/a/@href').extract()[0]
        #try(prev_link != None):
        #    yield scrapy.Request(prev_url, callback = self.parse_indetail)
        #except:
        #    logger.info('No previous pages to go to')



    def parse_indetail(self,response):
    	item = NewimdbcrawlerItem()
        item['title'] = response.xpath('//div[@class="title_wrapper"]/h1/text()').extract()[0][:-1]
        item['directors'] = response.xpath('//div[@class="credit_summary_item"]/span[@itemprop="director"]/a/span/text()').extract()[0]
        item['writers'] = response.xpath('//div[@class="credit_summary_item"]/span[@itemprop="creator"]/a/span/text()').extract()
        item['stars'] = response.xpath('//div[@class="credit_summary_item"]/span[@itemprop="actors"]/a/span/text()').extract()
        item['popularity'] = response.xpath('//div[@class="titleReviewBarSubItem"]/div/span/text()').extract()[2][21:-8]
        item['rating'] = response.meta['rating']
        return item


