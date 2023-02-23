import scrapy


class Jumia2Spider(scrapy.Spider):
    name = "jumia_2"
    
    def start_requests(self):
        for page_number in range(1,51):
            url = f'https://www.jumia.com.tn/telephone-tablette/?page={page_number}#catalog-listing'

            yield scrapy.Request(
                url=url,
                callback = self.parse_urls,
                meta = {
                    'url': url
                }
            )

    def parse_urls(self, response):
        articles = response.css('article')


        for article in articles:
            item_url = f'https://www.jumia.com.tn{article.css("a::attr(href)").get()}'
            item_price = article.css('.old::text').get()
            
            yield scrapy.Request(
                    url = item_url,
                    callback=self.parse
                )


    def parse(self, response):
        item = {}
        item['description'] = response.css('.markup.-mhm.-pvl.-oxa.-sc').get()
        yield item
