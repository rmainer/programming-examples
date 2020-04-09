#!/usr/bin/python3

# logging to a file and stdout

import logging
import sys

logging.root.handlers = []
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('/tmp/debug.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logging.info('information')
logging.warning('warning')
logging.error('error')
