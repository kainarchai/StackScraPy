# -*- coding: utf-8 -*-
import scrapy


class StackbotSpider(scrapy.Spider):
    name = 'stackbot'
    with open("urls.txt", "rt") as f:
        start_urls = [url.replace('"', '').replace(',', '').strip() for url in f.readlines()]


    def parse(self, response):
        for app in response.css('div.thumbnail-home'):
            yield {
                'stack-name': response.css('ol.breadcrumb.col-md-10.col-xs-12.bread-nav span::text')[0].extract(),
                'category-name': response.css('ol.breadcrumb.col-md-10.col-xs-12.bread-nav span::text')[1].extract(),
                'group-name': response.css('ol.breadcrumb.col-md-10.col-xs-12.bread-nav span::text')[2].extract(),
                'title': app.css('div.landing-stack-name span::text').extract_first(),
                'description': app.css('div.service-logo a::attr(data-hint)').extract_first(),
                'icon-url': app.css('div.service-logo img::attr(src)').extract_first(),
                'url': 'https://stackshare.io' + app.css('div.service-logo a::attr(href)').extract_first(),
            }
