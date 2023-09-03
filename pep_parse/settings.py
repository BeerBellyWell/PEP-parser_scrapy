import datetime as dt

from pathlib import Path


BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
ALLOWED_DOMAINS = 'peps.python.org'
UTF_8 = 'utf-8'
CSV = 'csv'
ROBOTSTXT_OBEY = True


FEEDS = {
    f'results/pep_%(time)s.{CSV}': {
        'format': f'{CSV}',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
NOW = dt.datetime.now()
NOW_FORMATTED = NOW.strftime(DATETIME_FORMAT)
BASE_DIR = Path(__file__).parent.parent
