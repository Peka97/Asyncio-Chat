import argparse
import logging
from socket import *

import log.config.client_log_config
from log.decorator import Log
from utils.send_to_server import send_to_server
from utils.get_from_server import get_from_server


LOGGER = logging.getLogger('client')


def start(args: argparse.ArgumentParser) -> None:
    """Client for messaging with servers.

    Args:
        args (argparse.ArgumentParser): Server IP and Server Port
    """
    addr, port, mode = args.address, args.port, args.mode

    client = socket(AF_INET, SOCK_STREAM)
    # client.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    if mode == 'R':
        LOGGER.info('Read Mode')
        get_from_server(client, addr, port)
    elif mode == 'W':
        LOGGER.info('Write Mode')
        send_to_server(client, addr, port)

    client.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=' > Send message to server.')
    parser.add_argument('address', type=str, help='Server IP.')
    parser.add_argument('port', default=7777, type=int, help='Server Port.')
    parser.add_argument('mode', type=str, default='R',
                        help='(R)ead or (W)rite mode')
    args = parser.parse_args()

    start(args)
