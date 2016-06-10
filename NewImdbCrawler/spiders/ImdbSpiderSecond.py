# -*- coding: utf-8 -*-
import scrapy
import logging
from NewImdbCrawler.items import NewimdbcrawlerItem

class SecondSpiderSpider(scrapy.Spider):
    name = "imdbspidergo2"
    allowed_domains = ["imdb.com"]
    start_urls = (
        'http://www.imdb.com/movies-coming-soon/',
    )   

    def parse(self, response):
        links = response.xpath('//div[@class="list detail"]/div/table/tbody/tr/td[2]/h4/a/@href').extract()
        i =1 
        for link in links:
            abs_url = response.urljoin(link)
            genre_url= '//div[@class="list detail"]/div[' + str(i) + ']/table/tbody/tr[1]/td[2]/p/span'
            genre = response.xpath('genre_url').extract()
            if (i <= len(links)):
                i=i+1
            yield scrapy.Request(abs_url, callback = self.parse_indetail, meta={'genre' : genre})
        prev_link=response.xpath('//div[@class="sort"]/a/@href').extract()[0]
        if prev_link:
            abs_prev_link=response.urljoin(prev_link)
            yield scrapy.Request(abs_prev_link, callback = self.parse)
        else:
            logger.info('No previous pages to go to')



    def parse_indetail(self,response):
        deeper_link = response.xpath('//div[@class="see-more"]/a/@href').extract()
        for thisthing in deeper_link:
            if thisthing.startswith('fullcredits'):
                index_this = deeper_link.index(thisthing)
        item = NewimdbcrawlerItem()
        abs_deeper_link=response.urljoin(deeper_link[index_this])
        #print '<---------------------------------------00000000000---------------------------------------------->'
        item['title'] = response.xpath('//div[@class="title_wrapper"]/h1/text()').extract()[0][:-1]
        item['directors'] = response.xpath('//div[@class="credit_summary_item"]/span[@itemprop="director"]/a/span/text()').extract()[0]
        item['writers'] = response.xpath('//div[@class="credit_summary_item"]/span[@itemprop="creator"]/a/span/text()').extract()
        item['stars'] = response.xpath('//div[@class="credit_summary_item"]/span[@itemprop="actors"]/a/span/text()').extract()
        item['popularity'] = response.xpath('//div[@class="titleReviewBarSubItem"]/div/span/text()').extract()
        item['genre'] = response.meta['genre']
        item['rating'] = response.xpath('//div[@class="ratingValue"]/strong/span/text()').extract()
        item['description'] = response.xpath('//div[@class="summary_text"]/text()').extract()
        item['releasedate'] =response.xpath('//div[@class="subtext"]/a[4]/text()').extract()
        item['totalrating'] =response.xpath('//div[@class="imdbRating"]/a/span/text()').extract()
        item['company'] = response.xpath('//div[@id="titleDetails"]/div[@class="txt-block"]/span[1]/a/span/text()').extract()
        item['image_urls']= response.xpath('//div[@class="poster"]/a/img/@src').extract()
        yield scrapy.Request(abs_deeper_link, callback = self.parse_moreindetail, meta=item)
        

    def parse_moreindetail(self,response):
    	item = NewimdbcrawlerItem()
        item['total_cast'] = response.xpath('//table[@class="cast_list"]/tr/td[2]/a/span/text()').extract()
        item['title'] = response.meta['title']
        item['directors'] = response.meta['directors']
        item['writers'] = response.meta['writers']
        item['stars'] = response.meta['stars']
        item['popularity'] = response.meta['popularity']
        item['genre'] = response.meta['genre']
        item['rating'] = response.meta['rating']
        item['description'] = response.meta['description']
        item['releasedate'] = response.meta['releasedate']
        item['totalrating'] = response.meta['totalrating']
        item['company'] = response.meta['company']
        item['image_urls']= response.meta['image_urls']
        return item


