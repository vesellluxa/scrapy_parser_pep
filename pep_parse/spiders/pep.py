import os
import re
import scrapy

from pep_parse.settings import BASE_DIR, RESULTS
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://' + domain + '/' for domain in allowed_domains]

    def __init__(self):
        super(scrapy.Spider, self).__init__()
        os.makedirs(os.path.dirname(BASE_DIR / RESULTS), exist_ok=True)

    def parse(self, response):
        peps = response.css('section#numerical-index td a::attr(href)')
        for pep_link in peps:
            yield response.follow(
                pep_link,
                callback=self.parse_pep
            )

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get().replace('-', '')
        number, name = re.search(
            r'PEP\s(?P<number>\d+)\W+(?P<name>.+)$',
            title
        ).groups()
        yield PepParseItem(
            {
                'number': number,
                'name': name,
                'status': response.css(
                    'dt:contains("Status") + dd abbr::text'
                ).get(),
            }
        )
