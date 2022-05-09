# -*- coding: utf-8 -*-
import json
from datetime import datetime

from bs4 import BeautifulSoup
import scrapy
import re
# from news_scrapy import settings
from django.utils import tree
from scrapy.spiders import Rule, CrawlSpider

from scrapy.linkextractors import LinkExtractor

from common.models import Post


class WangyiSpider(CrawlSpider):
    name = 'myscrape'
    allowed_domains = ['163.com']

    start_urls = ['http://news.163.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*\.163\.com/\d{2}/\d{4}/\d{2}/.*\.html'), callback='parse', follow=True),
    )

    def parse(self, response):
        content = '<br>'.join(response.css('.post_content p::text').getall())
        # content = '<br>'.join(response.css('.post_text p::text').getall())
        # print(content, "===============================content")
        if len(content) < 100:
            return

        print("Test==================================================")
        title = response.css('h1::text').get()
        print(title, "=========title")
        category = response.css('.post_crumb a::text').getall()[-1]
        print(category, "=======category")
        time_text = response.css('.post_info::text').get()
        timestamp_text = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', time_text).group()
        timestamp = datetime.fromisoformat(timestamp_text)
        # category = response.css('.post_crumb a::text').getall()[-1]
        print(timestamp, "==========================timestamp")
        Post.objects.create(
            title=title,
            timestamp=timestamp,
            category=category,
            # content=json.loads(content),
            content=content,
            url=response.url,
        )
