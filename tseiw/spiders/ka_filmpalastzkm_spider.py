# -*- coding: utf-8 -*-

import scrapy

from tseiw.items import TseiwItem, CinemaItem, MovieItem

class KAFilmpalastZKMSpider(scrapy.Spider):
    name = "KAFilmpalastZKM"
    allowed_domains = ["filmpalast.net"]
    start_urls = [
        "http://www.filmpalast.net/programm.html",
        "http://www.filmpalast.net/programm-folgewoche.html"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        #prepare cinema
        cinema = CinemaItem()
        cinema['name'] = "Filmpalast am ZKM"
        cinema['street'] = "Brauerstraße"
        cinema['streetNo'] = "40"
        cinema['postalCode'] = "76135"
        cinema['city'] = "Karlsruhe"
        cinema['country'] = "Germany"
        cinema['homepage'] = "http://www.filmpalast.net/"

        for movierow in response.css('article.film'):
          movie = MovieItem()
          movie['titleRaw'] = movierow.css('div > a > header > h3.gwfilmdb-film-title').xpath('text()').extract()[0]
          for screening in movierow.css('div.tab-content div.release-type-hdov table.programm-table tbody td.slot-future' 
            ', div.tab-content div.release-type-imaxov  table.programm-table tbody td.slot-future'
            ', div.tab-content div.release-type-3dov  table.programm-table tbody td.slot-future'
            ', div.tab-content div.release-type-imax3dov  table.programm-table tbody td.slot-future'):
            datetime = screening.css('div.modal-header h4.modal-title span').xpath('text()').extract()[0]
            features = screening.xpath('../../../../@class').extract()[0]
            link = screening.css('a.performance-popover').xpath('@href').extract()[0]
            item = TseiwItem()
            if 'release-type-imax3dov' in features:
              item['threeD'] = True
              item['imax'] = True
            elif 'release-type-3dov' in features:
              item['threeD'] = True
            elif 'release-type-imaxov' in features:
              item['imax'] = True
            item['datetime'] = datetime
            item['movie'] = dict(movie)
            item['link'] = link 
            item['cinema'] = dict(cinema)
            yield item