import csv
from collections import Counter
from datetime import datetime as dt

from pep_parse.settings import (BASE_DIR, RESULTS,
                                SUMMARY_TABLE_HEADER,
                                SUMMARY_TABLE_BOTTOM)

FILENAME = 'status_summary_{}.csv'
TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def open_spider(self, spider):
        self.total = Counter()
        self.time = dt.now().strftime(TIME_FORMAT)

    def process_item(self, item, spider):
        self.total[item['status']] += 1
        return item

    def close_spider(self, spider):
        with csv.writer(
            open(
                BASE_DIR / RESULTS / FILENAME.format(self.time),
                'w'
            )
        ) as file:
            file.writerow(SUMMARY_TABLE_HEADER, self.total.items())
            self.total[SUMMARY_TABLE_BOTTOM] = sum(self.total.values())
