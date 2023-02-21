import scrapy


class TunisieannonceSpider(scrapy.Spider):
    name = "tunisieannonce"
    def start_requests(self):
        pages =  ['http://www.tunisie-annonce.com/AnnoncesImmobilier.asp']
        for page_url in pages:
            yield scrapy.Request(
                url = page_url,
                callback = self.parse,
                meta = {
                    'url': page_url
                },
                errback = self.errback
            )

    def parse(self, response):
        posts = response.css('table a::text').getall()
        for post in posts:
            item = {}
            item['url'] = response.meta['url']
            item['title'] = post
            yield item

    def errback(self,failure):
        pass