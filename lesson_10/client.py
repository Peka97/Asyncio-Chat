from time import sleep
from threading import Thread
from socket import *

from metaclasses.client import ClientVerifier
from designs.connect import Ui_Connect


class Client(metaclass=ClientVerifier):
    _working = True

    # Для проверки ClientVetifier:
    # s = socket()

    def __init__(self, addr: str = '', port: int = 7777) -> None:
        self.addr = addr
        self.port = port

        self.socket = socket(AF_INET, SOCK_STREAM)

        # Для проверки ClientVetifier:
        # self.socket = socket(AF_INET, SOCK_DGRAM)

    def _write_loop(self):
        while True:
            message = input('Enter your Message: ').encode('utf-8')
            self.socket.send(message)

    def _read_loop(self):
        while True:
            message = self.socket.recv(1024).decode('utf-8')
            print(f'\n{message}')

    def start(self):
        # Для проверки ClientVetifier:
        # self.socket.accept()

        ui = 

        self.socket.connect((self.addr, self.port))
        read_thread = Thread(target=self._read_loop,
                             daemon=True)
        write_thread = Thread(target=self._write_loop,
                              daemon=True)

        read_thread.start()
        write_thread.start()

        while self._working and (read_thread.is_alive() and write_thread.is_alive()):
            sleep(1)

        self.socket.close()

    def stop(self):
        self._working = False
        self.socket.close()

    def stop(self):
        self.socket.close()


if __name__ == '__main__':
    client = Client()

    try:
        client.start()
    except KeyboardInterrupt:
        client.stop()
