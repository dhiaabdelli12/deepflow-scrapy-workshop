import scrapy


class GeniusSpider(scrapy.Spider):
    name = "genius"

    def start_requests(self):
        for page_number in range(1,5):
            page_url = f'https://genius.com/songs/all?page={page_number}'
            yield scrapy.Request(
                url = page_url,
                callback = self.parse,
                meta = {
                    'url': page_url
                },
                errback = self.errback
            )
    def parse(self, response):
        for title in response.css('li a span span::text').getall():
            item = {}
            item['url'] = response.meta['url']
            item['title'] = title
            yield item 

    def errback(self,failure):
        pass
