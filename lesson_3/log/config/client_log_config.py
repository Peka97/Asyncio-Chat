import logging
import logging.handlers
import os
import sys

date_format = '%Y-%m-%d %H:%M:%S'
CLI_FORMATTER = logging.Formatter(
    '%(asctime)s - [%(levelname)s] - %(filename)s | %(message)s',
    date_format
)

FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/client.log'

STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(CLI_FORMATTER)
STREAM_HANDLER.setLevel(logging.INFO)

LOG_FILE = logging.handlers.TimedRotatingFileHandler(
    FILE_PATH, encoding='utf8', interval=1, when='midnight')
LOG_FILE.setFormatter(CLI_FORMATTER)
LOG_FILE.setLevel(logging.ERROR)

LOGGER = logging.getLogger('client')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(logging.INFO)

if __name__ == '__main__':
    LOGGER.debug('CLIENT | Debug test message')
    LOGGER.info('CLIENT | Info test message')
    LOGGER.warning('CLIENT | Warning test message')
    LOGGER.error('CLIENT | Error test message')
    LOGGER.critical('CLIENT | Critical test message')
