import json
from time import sleep, time
from threading import Thread
from socket import *

from metaclasses.client import ClientVerifier
from designs.connect import Ui_Connect
from messages import Message
from database.db import ClientDatabase


class Client(metaclass=ClientVerifier):
    _working = True

    # Для проверки ClientVetifier:
    # s = socket()

    def __init__(
        self, addr: str = '',
        port: int | str = 7777,
        username: str = None,
        password: str = None
    ) -> None:
        self.addr = addr
        self.port = port
        self.username = username
        self.password = password
        self.db = ClientDatabase(username)

        self.socket = socket(AF_INET, SOCK_STREAM)

        # Для проверки ClientVetifier:
        # self.socket = socket(AF_INET, SOCK_DGRAM)

    def _auth(self):
        print('Авторизуюсь...')
        try:
            self.socket.connect((self.addr, int(self.port)))
        except ConnectionRefusedError:
            print('Сервер не запущен')
            exit()

        self.socket.send(Message.auth(self.username, self.password))
        answer = json.loads(self.socket.recv(1024).decode('utf-8'))
        if answer.get('response') and ['response'] != 200:
            return False
        return True

    def _update_contacts(self):
        print('Обновляю контакты...')
        message = Message.get_contacts(self.username)
        self.socket.send(message)

        answer = json.loads(self.socket.recv(1024).decode('utf-8'))
        print(answer)
        if answer.get('response') and answer['response'] == '202':
            friend_ids = answer['alert']
            if friend_ids:
                for id in friend_ids:
                    self.db.contact_add(id)

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
        self._auth()
        self._update_contacts()

        # read_thread = Thread(target=self._read_loop,
        #                      daemon=True)
        # write_thread = Thread(target=self._write_loop,
        #                       daemon=True)

        # read_thread.start()
        # write_thread.start()

        # while self._working and (read_thread.is_alive() and write_thread.is_alive()):
        #     sleep(1)

        # self.socket.close()

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
