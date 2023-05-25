import argparse
import json
from time import time
from socket import *
from pprint import pprint


def get_presence_msg() -> None:

    result = json.dumps({
        "action": "presence",
        "time": time(),
        "type": "status",
        "user": {
            "account_name": "Peka97",
            "status": "Hello, Server!"
        }
    }).encode('utf-8')
    return result


def start(args) -> None:
    addr, port = args.address, args.port

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((addr, port))

    request = get_presence_msg()

    s.sendto(request, (addr, port))
    responce = json.loads(s.recv(1000).decode('utf-8'))
    print('Server Responce:')
    pprint(responce)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=' > Send message to server.')
    parser.add_argument('address', type=str, help='Server IP.')
    parser.add_argument('port', default=7777, type=int, help='Server Port.')
    args = parser.parse_args()

    start(args)
