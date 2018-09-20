# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import PyRSS2Gen
import datetime
from .items import RssclientItem


rss = PyRSS2Gen.RSS2(
   title="Raymond's PyRSS2Gen feed",
   link="http://47.75.7.60:6379",
   description= "Raymond private subscription Rss",
   lastBuildDate=datetime.datetime.now(),
   items=[]
)


class RssclientPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item["rss"], PyRSS2Gen.RSS2):
            self.process_rss(item["rss"])
        return item

    def process_rss(self, item):
        item.write_xml(open("webapi/rss_xml/rssswitch.xml", "w", encoding='utf-8'), encoding='utf-8')
