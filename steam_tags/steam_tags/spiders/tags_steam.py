import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class SteamSpider(CrawlSpider):
    name = 'steam'
    allowed_domains = ['store.steampowered.com']
    start_urls = ['https://store.steampowered.com/search/?filter=topsellers']

    rules = (
        Rule(LinkExtractor(allow=r'/app/'),
             callback='parse_game', follow=True),
    )

    game_counter = 0

    def parse_game(self, response):
        if 'game_area_purchase_game' in\
                response.body.decode('utf-8'):
            tags = []
            for tag in response.css('.app_tag::text').getall():
                tag = tag.strip()
                if tag:
                    tags.append(tag)
            for section in response.css('.glance_tags.popular_tags'):
                for tag in section.css('.app_tag::text').getall():
                    tag = tag.strip()
                    if tag:
                        tags.append(tag)

            if self.game_counter < 10:
                with open('steam_tags.csv', 'a') as f:
                    f.write(','.join(tags) + '\n')
                self.game_counter += 1

                if self.game_counter == 1000:
                    raise scrapy.exceptions.CloseSpider\
                        ('First 10 games recorded')


if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess(settings={
        'FEEDS': {'steam_tags.csv': {'format': 'csv'}},
        'LOG_ENABLED': False
        
    })

    process.crawl(SteamSpider)
    process.start()
