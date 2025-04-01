# Basic Logging: Write a Python program that uses the logging module to log messages at different levels

import logging

# Set basic configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] - %(message)s',
    datefmt='%d %b %Y - %H:%M:%S'
)

# Create logger
logger = logging.getLogger(__name__)

# Log messages
logger.debug('Message')
logger.info('Message')
logger.warning('Message')
logger.error('Message')
logger.critical('Message')
