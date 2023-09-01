import scrapy

from scrapy.http.request import Request
from scrapy.http.response.html import HtmlResponse

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response: HtmlResponse) -> Request:
        """Парсинг ссылок на PEP docs"""
        tr_tags = response.css('section[id=numerical-index] tbody tr')
        all_peps = tr_tags.css('a[href^="pep"]')
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response: HtmlResponse) -> PepParseItem:
        """Парсинг данных со страницы PEP"""
        num_and_name = response.css(
            'section[id=pep-content] h1::text').get().split(' – ')
        num = num_and_name[0].split(' ')[1]
        name = num_and_name[1]
        data = {
            'number': int(num),
            'name': name,
            'status': response.css('abbr::text').get()
        }
        yield PepParseItem(data)
