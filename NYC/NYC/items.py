# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
# define the fields for your item here like:
class NycItem(scrapy.Item):
	d_year = scrapy.Field()
	d_total = scrapy.Field()
	d_domestic = scrapy.Field()
	d_int = scrapy.Field()
	e_year = scrapy.Field()
	e_direct_spend = scrapy.Field()
	e_total_jobs = scrapy.Field()
	e_wages = scrapy.Field()
	e_taxes = scrapy.Field()
	hotel_year = scrapy.Field()
	hotel_aho = scrapy.Field()
	hotel_adr = scrapy.Field()
	country = scrapy.Field()
	year13 = scrapy.Field()
	year14 = scrapy.Field()
	year15 = scrapy.Field()
	year16 = scrapy.Field()
	year17 = scrapy.Field()
	year18 = scrapy.Field()