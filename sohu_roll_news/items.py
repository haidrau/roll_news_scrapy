# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.item import Item,Field

class SohuRollNewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    
class LinkItem(Item):
	title=Field()
	link=Field()
	type=Field()
	time=Field()
        _id =Field()
        date=Field()	