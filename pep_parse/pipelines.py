import csv
import os

from collections import Counter
from datetime import datetime as dt

from pep_parse.settings import (RESULTS, BASE_DIR,
                                SUMMARY_TABLE_HEADER,
                                SUMMARY_TABLE_BOTTOM)

FILENAME = 'status_summary_{}.csv'
TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses_count = Counter()

    def process_item(self, item, spider):
        self.statuses_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(
                BASE_DIR / RESULTS / FILENAME.format(
                    dt.now().strftime(TIME_FORMAT)),
                'w'
        ) as file:
            csv.writer(file).writerows(
                [
                    *[SUMMARY_TABLE_HEADER,
                      *self.statuses_count.items(),
                      SUMMARY_TABLE_BOTTOM + [self.statuses_count.total()]]
                ]
            )
