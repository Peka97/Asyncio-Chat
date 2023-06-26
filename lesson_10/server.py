from socket import *
from select import select

from metaclasses.server import ServerVerifier
from descriptors.port import Port
from database.db import Database


class Server(metaclass=ServerVerifier):
    port = Port()
    db = Database()

    def __init__(self, addr: str = '', port: int = 7777) -> None:
        self.addr = addr
        self.port = port

        # Для проверки ServerVerifier:
        # self.socket = socket(AF_INET, SOCK_DGRAM)

        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((self.addr, self.port))
        self.socket.listen(5)
        self.socket.settimeout(1)

        self.clients = []

    @staticmethod
    def read_message(socket: socket):
        return socket.recv(1024).decode('utf-8')

    @staticmethod
    def send_message(socket: socket, message: str):
        socket.send(message.encode('utf-8'))

    def start(self):
        # Для проверки ServerVerifier:
        # self.socket.connect()

        while True:
            try:
                client, addr_info = self.socket.accept()
                client_addr, client_port = addr_info

                # Делаем запись в БД о подключении
                self.db.history_update(client_addr, client_port)
            except OSError as err:
                pass
            else:
                self.clients.append(client)
            finally:
                try:
                    i_cli, o_cli, e_cli = select(
                        self.clients,
                        self.clients,
                        [],
                        0
                    )
                except Exception:
                    pass

                messages = []  # Обнуляем список сообщений

                for client in i_cli:
                    message = self.read_message(client)
                    if message:  # Исключаем пустые строки
                        messages.append(message)

                if messages:  # Проверяем есть ли сообщения
                    for message in messages:
                        for client in o_cli:
                            try:
                                self.send_message(client, message)
                            except Exception:
                                self.clients.remove(client)

    def stop(self):
        self.socket.close()


if __name__ == '__main__':
    server = Server()

    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
