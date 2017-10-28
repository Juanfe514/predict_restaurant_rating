#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:34:34 2017

@author: juanfelipegonzalez
"""

import scrapy



class getAllinfos(scrapy.Spider) :
    name = 'getallinfos'

    def __init__(self, *args, **kwargs): 
      super(getAllinfos, self).__init__(*args, **kwargs)

      self.start_urls = [kwargs.get('start_url')]

    def parse(self, response):
        allinfos = response.css("div#RESTAURANT_DETAILS")
        yield {'allinfo' : 'a'+ allinfos.css('div').extract_first()}

  