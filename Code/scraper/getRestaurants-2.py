import scrapy

class getRestaurants(scrapy.Spider):
    name = 'getrestaurants’

    def __init__(self, *args, **kwargs): 
      super(getHotels, self).__init__(*args, **kwargs) 

      self.start_urls = [kwargs.get('start_url')]

    def parse(self, response):
        for hotel in response.css("div.shortSellDetails"):
            yield {'hotel': hotel.css('a ::attr(href)').extract_first()}

        next_page = response.css('div.unified.pagination > a ::attr(href)').extract()[-1]
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)