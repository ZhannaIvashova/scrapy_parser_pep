import csv

from collections import defaultdict
from datetime import datetime

from pep_parse.settings import BASE_DIR


DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / 'results'
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.count = defaultdict(int)

    def process_item(self, item, spider):
        self.count[item['status']] += 1
        return item

    def close_spider(self, spider):
        current_time = datetime.now().strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{current_time}.csv'
        file_path = self.results_dir / file_name
        with open(file_path, mode='w', encoding='utf-8') as csvfile:
            writer = csv.writer(
                csvfile, dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE, escapechar='\\'
            )
            writer.writerow(('Статус', 'Количество'))
            for status, count in self.count.items():
                writer.writerow([status, count])
            writer.writerow(('Всего', sum(self.count.values())))
