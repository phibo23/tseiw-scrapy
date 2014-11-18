# -*- coding: utf-8 -*-

import scrapy

from tseiw.items import TseiwItem, CinemaItem, MovieItem

class KASchauburgSpider(scrapy.Spider):
    name = "KASchauburg"
    allowed_domains = ["schauburg.de"]
    start_urls = [
        "http://schauburg.de/programm.php"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        #prepare cinema
        cinema = CinemaItem()
        cinema['name'] = "Filmtheater Schauburg"
        cinema['street'] = "Marienstraße"
        cinema['streetNo'] = "16"
        cinema['postalCode'] = "76137"
        cinema['city'] = "Karlsruhe"
        cinema['country'] = "Germany"
        cinema['homepage'] = "http://schauburg.de/"

        triggers = [
            "englisches Original",
            "OmU",
            "Originalfassung"
        ]

        fourKTriggers = [
            "in 4K Ultra-High-Definition"
        ]
        omuTriggers = [
            "mit dt. Untertitel",
            "mit dt. Untertiteln",
            "mit deutschen Untertiteln",
            "OmU"
        ]

        for movierow in response.xpath('/html/body/table/tr'):
            raw = movierow.xpath('td[2]').extract()[0]
            if any(trigger in raw for trigger in triggers):
                movie = MovieItem()
                movie['titleRaw'] = movierow.xpath('td[2]/a[1]/text()').extract()[0]
                date = movierow.xpath('../preceding-sibling::h5[1]/text()').extract()[0]
                time = movierow.xpath('td[1]/text()').extract()[0]
                link = movierow.xpath('td[2]/a/@href').extract()[0]
                item = TseiwItem()
                item['cinema'] = cinema
                item['movie'] = movie
                item['link'] = cinema['homepage'] + link
                item['datetime'] = date.split(',')[-1].strip() + ' ' + time
                if any(fourK in raw for fourK in fourKTriggers):
                    item['fourK'] = True
                if any(omu in raw for omu in omuTriggers):
                    item['omu'] = True
                yield item