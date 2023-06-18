import csv
import os

from collections import Counter
from datetime import datetime as dt

from pep_parse.settings import (BASE_DIR, RESULTS,
                                SUMMARY_TABLE_HEADER)

FILENAME = 'status_summary_{}.csv'
TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses_count = Counter()

    def process_item(self, item, spider):
        self.statuses_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        file_path = BASE_DIR / RESULTS / FILENAME.format(
            dt.now().strftime(TIME_FORMAT))
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(
                file_path,
                'w'
        ) as file:
            csv.writer(file).writerows(
                [*[SUMMARY_TABLE_HEADER, *self.statuses_count.items()]]
            )
