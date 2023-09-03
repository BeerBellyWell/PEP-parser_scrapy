from scrapy import signals, Item
from scrapy.crawler import Crawler
from scrapy.http.response.html import HtmlResponse
from typing import Union, Generator
from scrapy.http.request import Request

from pep_parse.spiders.pep import PepSpider


class PepParseSpiderMiddleware:

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> 'PepParseSpiderMiddleware':
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response: HtmlResponse,
                             spider: PepSpider) -> None:
        return None

    def process_spider_output(self, response: HtmlResponse,
                              result: Union[Request, Item],
                              spider: PepSpider) -> Generator[Request, Item]:
        for i in result:
            yield i

    def process_spider_exception(self, response: HtmlResponse,
                                 exception: Exception,
                                 spider: PepSpider) -> None:
        pass

    def process_start_requests(self, start_requests: Request,
                               spider: PepSpider) -> Generator[Request, ]:
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class PepParseDownloaderMiddleware:
    @classmethod
    def from_crawler(cls, crawler: Crawler) -> 'PepParseDownloaderMiddleware':
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request: Request,
                        spider: PepSpider) -> None:
        return None

    def process_response(self, request: Request, response: HtmlResponse,
                         spider: PepSpider) -> HtmlResponse:
        return response

    def process_exception(self, request: Request, exception: Exception,
                          spider: PepSpider) -> None:
        pass

    def spider_opened(self, spider: PepSpider) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)
