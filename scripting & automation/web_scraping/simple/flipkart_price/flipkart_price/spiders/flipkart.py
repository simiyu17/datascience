# -*- coding: utf-8 -*-
import scrapy
import pandas as pd


class FlipkartSpider(scrapy.Spider):
    name = 'flipkart'
    allowed_domains = ['flipkart.com']
    start_urls = ['https://www.flipkart.com/laptops/~gaming/pr?count=40&p%5B%5D=sort%3Dpopularity&sid=6bo%2Fb5g&wid=2.productCard.PMU_V2_2']

    def parse(self, response):
        for laptop in response.xpath('//div[@class="bhgxx2"]'):
            prices = []

            for p in laptop.xpath('//div[@class="_1vC4OE _2rQ-NK"]/text()').extract():
                prices.append(price_convert(p))

            laptop_item = {
                'name': laptop.xpath('//div[@class="_3wU53n"]/text()').extract(),
                'price': prices,
                'review': laptop.xpath('//div[@class="hGSR34"]/text()').extract()
            }

            df = pd.DataFrame(laptop_item, columns=['name','price','review'])
            df.set_index('name')

            yield df.to_csv("laptop_prices.csv",sep=",")


def price_convert(number):
    return float(number.replace(',', '').replace('₹', '', ))