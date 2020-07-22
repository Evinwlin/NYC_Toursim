##scrapy on baruch
import re
from scrapy import Spider
from NYC.items import NycItem

class NycSpider(Spider):
	name = "NYC_spider"
	allowed_urls = ['https://www.baruch.cuny.edu/nycdata/tourism/index.html']

	start_urls = ['https://www.baruch.cuny.edu/nycdata/tourism/visitors.html']
	def parse (self, response):
		rows = response.xpath('//*[@id="myTable"]/tr')
		for row in rows[6:]:
			d_year = row.xpath ('./td[2]/text()').extract_first()
			d_total = row.xpath('./td[3]/div/text()').extract_first()
			d_domestic = row.xpath('./td[4]/div/text()').extract_first()
			d_int = row.xpath('./td[5]/div/text()').extract_first()

			item = NycItem()
			item['d_year'] = d_year
			item['d_total'] = d_total
			item['d_domestic'] = d_domestic
			item['d_int'] = d_int
			yield item
	
	start_urls = ['https://www.baruch.cuny.edu/nycdata/tourism/economic_impact.html']
	def parse (self, response):
		rows = response.xpath('//*[@id="myTable"]/tr')
		for row in rows[5:]:
			e_year = row.xpath ('./td[2]/div/text()').extract_first()
			e_direct_spend = row.xpath ('./td[3]/div/text()').extract_first()
			e_total_jobs = row.xpath('./td[4]/div/text()').extract_first()
			e_wages = row.xpath('./td[5]/div/text()').extract_first()
			e_taxes = row.xpath('./td[6]/div/text()').extract_first()

			item = NycItem()
			item['e_year'] = e_year
			item['e_direct_spend'] = e_direct_spend
			item['e_total_jobs'] = e_total_jobs
			item['e_wages'] = e_wages
			item['e_taxes'] = e_taxes
			yield item

	start_urls = ['https://www.baruch.cuny.edu/nycdata/tourism/hotel_market.html']
	def parse (self, response):
		rows = response.xpath('//*[@id="myTable"]/tr')
		for row in rows[5:]:
			hotel_year = row.xpath ('./td[2]/text()').extract_first()
			hotel_aho = row.xpath ('./td[3]/div/text()').extract_first()
			hotel_adr = row.xpath('./td[4]/div/text()').extract_first()

			item = NycItem()
			item['hotel_year'] = hotel_year
			item['hotel_aho'] = hotel_aho
			item['hotel_adr'] = hotel_adr 
			yield item

	start_urls = ['https://www.baruch.cuny.edu/nycdata/tourism/international_visitors.html']
	def parse (self, response):
		rows = response.xpath('//*[@id="myTable"]/tr')
		for row in rows[5:]:

			country = row.xpath ('./td[2]/text()').extract_first()
			year13 = row.xpath ('./td[3]/div/text()').extract_first()
			year14 = row.xpath('./td[4]/div/text()').extract_first()
			year15 = row.xpath('./td[5]/div/text()').extract_first()
			year16 = row.xpath('./td[6]/div/text()').extract_first()
			year17 = row.xpath('./td[7]/div/text()').extract_first()
			year18 = row.xpath('./td[8]/div/text()').extract_first()

			item = NycItem()
			item['country'] = country
			item['y13'] = year13
			item['y14'] = year14 
			item['y15'] = year15
			item['y16'] = year16
			item['y17'] = year17
			item['y18'] = year18
			yield item





