import csv
from collections import Counter
from datetime import datetime as dt
from scrapy.exceptions import DropItem

from pep_parse.settings import BASE_DIR

FILENAME = 'status_summary_{}.csv'
RESULTS_DIR = 'results'
TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def open_spider(self, spider):
        self.total = Counter()
        self.time = dt.now().strftime(TIME_FORMAT)

    def process_item(self, item, spider):
        if 'status' not in item:
            raise DropItem('Status не найден')
        self.total[item['status']] += 1
        return item

    def close_spider(self, spider):
        file = csv.writer(
            open(
                BASE_DIR / RESULTS_DIR / FILENAME.format(self.time),
                'w'
            )
        )
        file.writerow(['Статус', 'Количество'])
        self.total['Total'] = sum(self.total.values())
        file.writerows(self.total.items())
