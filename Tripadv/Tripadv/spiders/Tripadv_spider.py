## Scrapy on tripadvisor 

from scrapy import Spider, Request
from Tripadv.items import TripadvItem



class TripAdvisorSpider(Spider):
    name = 'tripadv_spider'
    allowed_domains = ['www.tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Attractions-g60763-Activities-a_allAttractions.true New_York_City_New_York.html']
    # 'https://www.tripadvisor.com/Attractions-g60763-Activities-oa30-New_York_City_New_York.html#FILTERED_LIST']
    


    def parse(self, response):

        First_page_url =["https://www.tripadvisor.com/Attractions-g60763-Activities-a_allAttractions.true-New_York_City_New_York.html"]
        
        for url in First_page_url:
            yield Request(url=url, callback=self.parse_result_page)

        # result_urls = ["https://www.tripadvisor.com/Attractions-g60763-Activities-oa{}0-New_York_City_New_York.html#FILTERED_LIST'.format(x) for x in range(3,120,3)"]
        # for url in result_urls:
        #     yield Request(url=url, callback=self.parse_result_page)
            

    def parse_result_page(self, response):
        product_urls = response.xpath('//div[@class="tracking_attraction_title listing_title "]/a/@href').extract()

        product_urls = ['https://www.tripadvisor.com' + x for x in product_urls]

        for url in product_urls:
            yield Request(url,callback=self.parse_detail_page)

    def parse_detail_page(self,response):
        try:
            rating = response.xpath('//span[@class="overallRating"]/text()').extract_first()
        except IndexError:
            rating = 0 
        try:
            numreviews = response.xpath('//*[@id="taplc_location_detail_reviews_card_0"]/div[2]/a[2]/text()').extract_first()
        except IndexError:
            numreviews = 0 
        types= response.xpath('//div[@class="detail"]/a[1]/text()').extract_first() +","+ response.xpath('//div[@class="detail"]/a[2]/text()').extract_first()
        title = response.xpath('//h1[@class="ui_header h1"]/text()').extract_first()

        
        item = TripadvItem()
        item['rating'] = rating
        item['numreviews'] = numreviews
        item['types'] = types
        item['title'] = title
        

        yield item