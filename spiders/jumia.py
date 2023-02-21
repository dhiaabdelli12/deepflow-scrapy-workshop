import scrapy


class JumiaSpider(scrapy.Spider):
    name = "jumia"

    def start_requests(self):
        pages = ['https://www.jumia.com.tn/telephone-tablette/']
        for page_url in pages:
            yield scrapy.Request(
                url=page_url,
                callback = self.parse,
                meta = {
                    'page_url': page_url
                },
                errback=self.errback
            )

    def parse(self, response):
        

        cards = response.css('h3.name::text') 
        for card in cards:
            item = {}
            item['url'] = response.meta['page_url']
            item['title'] = card.get()
            yield item

    def errback(self,failure):
        pass
