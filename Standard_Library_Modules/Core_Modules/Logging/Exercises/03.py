# Custom Formatting: Write a Python program that logs messages with a custom format, including the timestamp, log level, and message

import logging

# StreamHandler
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelno)s] - %(message)s',
    datefmt='%Y %b %d - %H:%M:%S'
)

# Logger
logger = logging.getLogger(__name__)

# FileHandler
handler = logging.FileHandler('logs.log')
formatter = logging.Formatter(
    '%(asctime)s [%(levelno)s] - %(message)s',
    datefmt='%Y %b %d - %H:%M:%S'
)

handler.setFormatter(formatter)
logger.addHandler(handler)

# Logs
logger.debug('Test 1')
logger.info('Test 2')
logger.warning('Test 3')
logger.error('Test 4')
logger.critical('Test 5')
