# File Logging: Write a Python program that logs messages to a file instead of the console

import logging

# StreamHandler configuration (default)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] - %(message)s)',
    datefmt='%Y %b %d - %H:%M:%S'
)

# Create logger
logger = logging.getLogger(__name__)

# Create handler and formatter
handler = logging.FileHandler('test.log')  # file
formatter = logging.Formatter(  # format
    '%(asctime)s [%(levelname)s] - %(message)s',
    datefmt='%Y %b %d - %H:%M:%S'
)

# Link formatter to handler, and handler to loggers
handler.setFormatter(formatter)
logger.addHandler(handler)

# Log messages
logger.info('Test 1')
logger.warning('Test 2')
logger.error('Test 1')
