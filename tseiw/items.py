# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TseiwItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    datetime = scrapy.Field()
    cinema = scrapy.Field()
    link = scrapy.Field()
    movie = scrapy.Field()
    threeD = scrapy.Field()
    
class CinemaItem(scrapy.Item):
	name = scrapy.Field()
	chain = scrapy.Field()
	street = scrapy.Field()
	streetNo = scrapy.Field()
	postalCode = scrapy.Field()
	city = scrapy.Field()
	country = scrapy.Field()
	homepage = scrapy.Field()

class MovieItem(scrapy.Item):
	titleRaw = scrapy.Field()
	title = scrapy.Field()
	imdbId = scrapy.Field()