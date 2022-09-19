import scrapy

# XPATH

# links = response.xpath('//a[starts-with(@href, "collection") and (parent::h3 | parent::h2)]/@href').getall()


class SpiderCIA(scrapy.Spider):
    name = 'cia'
    start_urls = [
        'https://www.cia.gov/readingroom/historical-collections'
    ]
    custom_settings = {
        'FEED_URI': 'cia.json',
        'FEED_FORMAT': 'json',
        'FEED:EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        links_desclassified = response.xpath(
            '//a[starts-with(@href, "collection") and (parent::h3 | parent::h2)]/@href').getall()
        for link in links_desclassified:
            yield response.follow(link, callback=self.parse_link)

    def parse_link(self, response):
        pass
