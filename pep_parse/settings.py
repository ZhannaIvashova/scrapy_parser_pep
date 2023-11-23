from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

NAME = 'pep'
ALLOWED_DOMAINS = ['peps.python.org']
STARS_URLS = ['https://peps.python.org/']

BASE_DIR = Path(__file__).parent.parent

ROBOTSTXT_OBEY = True

PEP_PIPELINE_PRIORITY = 300

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': PEP_PIPELINE_PRIORITY,
}
