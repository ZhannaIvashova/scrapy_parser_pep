import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps = response.css(
            '#numerical-index a.pep.reference.internal::attr(href)'
        ).getall()
        for pep_link in all_peps:
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
