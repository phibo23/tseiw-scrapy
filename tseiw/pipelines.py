# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import locale
from datetime import datetime
from tseiw.spiders.ka_filmpalastzkm_spider import KAFilmpalastZKMSpider
from tseiw.spiders.ka_schauburg_spider import KASchauburgSpider

class TseiwPipeline(object):
    def process_item(self, item, spider):
        return item

class DateTimePipeline(object):
	def process_item(self, item, spider):
		if isinstance(spider, KAFilmpalastZKMSpider):
			if item['datetime']:
				locale.setlocale(locale.LC_TIME,"de_DE")
				parsedDateTime = datetime.strptime(item['datetime'],'%a %d.%m. %H:%M Uhr')
				now = datetime.now()
				year = (parsedDateTime.month>=now.month) and now.year or now.year+1
				parsedDateTime = parsedDateTime.replace(year=year)
				item['datetime'] = parsedDateTime.isoformat()
		if isinstance(spider, KASchauburgSpider):
			if item['datetime']:
				locale.setlocale(locale.LC_TIME,"de_DE")
				parsedDateTime = datetime.strptime(item['datetime'],'%d.%m. %H.%M')
				now = datetime.now()
				year = (parsedDateTime.month>=now.month) and now.year or now.year+1
				parsedDateTime = parsedDateTime.replace(year=year)
				item['datetime'] = parsedDateTime.isoformat()

		return item

class MovieDetailsPipeline(object):
	def process_item(self, item, spider):
		#TODO: fetch original title, languages etc from tmdb or other api
		pass