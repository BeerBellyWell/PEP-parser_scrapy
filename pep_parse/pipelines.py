import csv

from pep_parse.settings import NOW_FORMATTED, BASE_DIR, CSV, UTF_8

from pep_parse.items import PepParseItem
from pep_parse.spiders.pep import PepSpider


class PepParsePipeline:

    def open_spider(self, spider: PepSpider) -> None:
        self.status_summary = {
            'Accepted': 0, 'Active': 0, 'Deferred': 0, 'Draft': 0,
            'Final': 0, 'Provisional': 0, 'Rejected': 0, 'Superseded': 0,
            'Withdrawn': 0, 'Total': 0
        }

    def process_item(self, item: PepParseItem,
                     spider: PepSpider) -> PepParseItem:
        if item['status'] in self.status_summary:
            self.status_summary[item['status']] += 1
            self.status_summary['Total'] += 1
        return item

    def close_spider(self, spider: PepSpider) -> None:
        RESULTS_DIR = BASE_DIR / 'results'
        FILE_NAME = f'status_summary_{NOW_FORMATTED}.{CSV}'
        FILE_PATH = RESULTS_DIR / FILE_NAME
        with open(FILE_PATH, mode='w', encoding=UTF_8) as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow(('Статус', 'Количество'))
            for k, v in self.status_summary.items():
                writer.writerow((k, v))
