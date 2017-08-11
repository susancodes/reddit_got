# -*- coding: utf-8 -*-
from pprint import pprint
from scrapy import Spider


class RedditGOT(Spider):
	name = 'redditGOT'
	allowed_domains = ['www.reddit.com/r/gameofthrones/']
	start_urls = ['https://www.reddit.com/r/gameofthrones/']

	def parse(self, response):
		# remember that .extract() returns a list
		page_title = response.css('title::text').extract()[0]
		
		topic_titles = response.css('.title.may-blank::text').extract()
		topic_comment_count = response.css('.comments.may-blank::text').extract()

		topics = []
		for item in zip(topic_titles, topic_comment_count):
			topics.append({
				'title': item[0],
				'comment_count': item[1]
				})

		scraped_dict = {
			'page_title': page_title,
			'topics': topics
		}

		return pprint(scraped_dict)
