import logging
import logging.handlers
import os
import sys

date_format = '%Y-%m-%d %H:%M:%S'
SERV_FORMATTER = logging.Formatter(
    '%(asctime)s - [%(levelname)s] - %(filename)s | %(message)s',
    date_format
)

FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/server.log'

STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERV_FORMATTER)
STREAM_HANDLER.setLevel(logging.DEBUG)

LOG_FILE = logging.handlers.TimedRotatingFileHandler(
    FILE_PATH, encoding='utf8', interval=1, when='midnight')
LOG_FILE.setFormatter(SERV_FORMATTER)
LOG_FILE.setLevel(logging.DEBUG)

LOGGER = logging.getLogger('server')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(logging.DEBUG)

if __name__ == '__main__':
    LOGGER.debug('SERVER | Debug test message')
    LOGGER.info('SERVER | Info test message')
    LOGGER.warning('SERVER | Warning test message')
    LOGGER.error('SERVER | Error test message')
    LOGGER.critical('SERVER | Critical test message')
