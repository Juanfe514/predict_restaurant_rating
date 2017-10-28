import scrapy
import re

x=re.compile(r'(.*)Reviews-')
y=re.compile(r'Reviews-(.*)')


class getComments(scrapy.Spider):
    name = 'getcomments'

    def __init__(self, *args, **kwargs): 
      super(getComments, self).__init__(*args, **kwargs)

      self.start_urls = [kwargs.get('start_url')]

    def parse(self, response):
        for comment in response.css("div.innerBubble > div.wrap"):
            if str(comment.css('a ::attr(href)').extract_first()) != "/apps":
                yield {'comment': comment.css('a ::attr(href)').extract_first()}
            else:
                yield {'comment': comment.css('a ::attr(href)').extract()[-1]}

#        if next_page:
#            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
#next_page = response.css('div.unified.pagination > a ::attr(href)').extract()[-1]