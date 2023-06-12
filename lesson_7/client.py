import argparse
import logging
from socket import *

from utils import read_message, send_message


def write_loop(client: socket):
    while True:
        message = input('Message: ').encode('utf-8')
        client.send(message)


def read_loop(client: socket):
    while True:
        message = client.recv(1024).decode('utf-8')
        print(message)


def main():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('', 7777))

    mode = input('Select mode (R)ead or (W)rite: ')
    if mode == 'R':
        read_loop(client)
    elif mode == 'W':
        write_loop(client)

    client.close()


if __name__ == '__main__':
    main()
