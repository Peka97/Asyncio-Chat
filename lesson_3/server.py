import json
import argparse
from time import time
from socket import *
from pprint import pprint


def start(args: argparse.ArgumentParser) -> None:
    """Server for messaging with clients.

    Args:
        args (argparse.ArgumentParser): Port to work and IP to listening.
    """

    port, addr = args.p, args.a
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((addr, port))
    s.listen(5)

    while True:
        client, addr_info = s.accept()
        client_addr, client_ip = addr_info

        try:
            msg = client.recv(1000)
            json_msg = json.loads(msg.decode('utf-8'))
            print(f"Client Message:")
            pprint(json_msg)
            response = {
                "response": 200,
                "time": time(),
            }
        except json.decoder.JSONDecodeError:
            response = {
                "response": 400,
                "time": time(),
                "alert": "Bad Request"
            }
        except Exception:
            response = {
                "response": 500,
                "time": time(),
                "alert": "Server Error"
            }

        print("\nServer Responce:")
        pprint(response)
        client.sendto(json.dumps(response).encode('utf-8'),
                      (client_addr, client_ip))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=' > Get messages from clients.')
    parser.add_argument('-p', default=7777, type=int, help='Server Port.')
    parser.add_argument('-a', default='', type=str,
                        help='Server IP to listening.')
    args = parser.parse_args()

    start(args)
