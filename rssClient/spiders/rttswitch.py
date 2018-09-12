# -*- coding: utf-8 -*-
import scrapy
from ..items import RssclientItem
import PyRSS2Gen
import datetime

rss = PyRSS2Gen.RSS2(
   title="Raymond's PyRSS2Gen feed",
   link="http://47.75.7.60:6379",
   description= "Raymond private subscription Rss",
   lastBuildDate=datetime.datetime.now(),
   items=[]
)


class RttswitchSpider(scrapy.Spider):
    name = 'rttswitch'
    start_urls = ['http://www.rttswitch.com/']

    def parse(self, response):
        pattern = "//h4[@class='eltd-post-title']/a/@href"
        for item in response.xpath(pattern).extract():
            yield scrapy.Request(item, self.parse_detail)

    def parse_detail(self, response):
        title_xpath = "//title/text()"
        detail_xpath = '//div[@class="eltd-text-holder"]'

        title = response.xpath(title_xpath).extract()[0].split("|")[0]
        detail = response.xpath(detail_xpath).extract()[0]
        date = response.xpath('//div[@class="eltd-post-info-date"]/text()').extract()[0].strip()
        url = response.url
        item = RssclientItem()
        rss_item = PyRSS2Gen.RSSItem(
            title=title,
            link=url,
            description=detail,
            guid=PyRSS2Gen.Guid(url),
            pubDate=datetime.datetime.strptime(date, '%Y-%m-%d'))
        rss.items.append(rss_item)
        item["rss"] = rss
        if len(rss.items) == 35:
            return item


