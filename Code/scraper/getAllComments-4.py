import scrapy



class getAllComments(scrapy.Spider) :
    name = 'getallcomments'

    def __init__(self, *args, **kwargs): 
      super(getAllComments, self).__init__(*args, **kwargs)

      self.start_urls = [kwargs.get('start_url')]

    def parse(self, response) :
        allcomment = response.css("div.innerBubble")
        yield {'allcomment' : allcomment.css('div').extract_first() + str(response.css("span.format_address").extract())}

               