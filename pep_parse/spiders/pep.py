import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS, NAME, STARS_URLS


class PepSpider(scrapy.Spider):
    name = NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = STARS_URLS

    def parse(self, response):
        all_peps = response.css(
            '#numerical-index a.pep.reference.internal::attr(href)'
        ).getall()
        for pep_link in all_peps:
            if not pep_link.endswith('/'):
                pep_link += '/'
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': response.css(
                'li:contains("PEP Index") + li::text'
            ).get().replace('PEP ', ''),
            'name': ' '.join(response.css(
                'h1.page-title::text').get().split(' ')[3:]),
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get()
        }
        yield PepParseItem(data)
