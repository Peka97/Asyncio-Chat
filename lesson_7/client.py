from time import sleep
from threading import Thread
from socket import *


def write_loop(client: socket):
    while True:
        message = input('Enter your Message: ').encode('utf-8')
        client.send(message)


def read_loop(client: socket):
    while True:
        message = client.recv(1024).decode('utf-8')
        print(f'\n{message}')


def main():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('', 7777))

    read_thread = Thread(target=read_loop, args=(client, ), daemon=True)
    write_thread = Thread(target=write_loop, args=(client, ), daemon=True)

    read_thread.start()
    write_thread.start()

    while read_thread.is_alive() and write_thread.is_alive():
        sleep(1)

    client.close()


if __name__ == '__main__':
    main()
