# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


def serialize_name(value):
    return ''.join(value).split("-")[0] if value else None

class FlipkartPriceItem(scrapy.Item):
    # define the fields for your item here like:
     name = scrapy.Field()#(serializer=serialize_name)
     price = scrapy.Field()
     review = scrapy.Field()

