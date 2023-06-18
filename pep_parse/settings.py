import os

from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']

PEP_SPIDER_URL = 'peps.python.org'

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent.parent

RESULTS = 'results'

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

FILE_FORMAT = 'csv'

SUMMARY_NAME = 'status_summary'
SUMMARY_TABLE_HEADER = ['Status', 'Quantity']
SUMMARY_TABLE_BOTTOM = ['Total']

PEP_NAME = 'pep'
PEP_FILE_NAME = f'{PEP_NAME}_%(time)s.{FILE_FORMAT}'

FEEDS = {
    f'{RESULTS}/{PEP_FILE_NAME}': {
        'format': FILE_FORMAT,
        'fields': ['number', 'name', 'status'],
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}


os.makedirs(os.path.dirname(BASE_DIR / RESULTS), exist_ok=True)
