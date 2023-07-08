import json
from time import time
from socket import *
from select import select
from traceback import format_exc

from metaclasses.server import ServerVerifier
from descriptors.port import Port
from database.db import ServerDatabase
from messages import Message


class Server(metaclass=ServerVerifier):
    """Server"""

    port = Port()

    def __init__(self, addr: str = '127.0.0.1', port: int = 7777) -> None:
        with open('server_config.json', 'r', encoding='utf-8') as fp:
            config = json.load(fp)
            self.db = ServerDatabase(config['db_path'])

        self.addr = addr
        self.port = port

        # Для проверки ServerVerifier:
        # self.socket = socket(AF_INET, SOCK_DGRAM)

        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((self.addr, self.port))
        self.socket.settimeout(1)
        self.socket.listen(5)

        self.clients = []

    def read_message(self, socket: socket):

        message = json.loads(socket.recv(1024).decode('utf-8'))
        answer = {
                        'response': 403,
                        'time': time()
                        }
        if message['action'] == 'auth':
            print('АВТОРИЗАЦИЯ ПОЛЬЗОВАТЕЛЯ')
            try:
                username = message['username']
                password = message['password']
                print(f'LOGIN: {username}')
                print(f'PSWD: {password}')

                if self.db.user_exists(username):
                    print('ПОЛЬЗОВАТЕЛЬ НАЙДЕН')
                    if self.db.user_auth(username, password):
                        print('ПОЛЬЗОВАТЕЛЬ АВТОРИЗОВАН')
                        answer = {
                        'response': 200,
                        'time': time()
                        }                    
            except Exception as err:
                pass
        elif message['action'] == 'get_contacts':
            username = message['username']
            print('Username: ' + username)
            contacts = self.db.user_get_contacts(username)
            print(f'Contacts: {contacts}')
            answer = Message.send_contacts(contacts)
        elif message['action'] == 'add_contact':
            answer = Message.add_contact()
        elif message['action'] == 'del_contact':
            answer = Message.del_contact()
        else:
            return
        
        if not isinstance(answer, bytes):
            answer = json.dumps(answer).encode('utf-8')
        print('ОТВЕТ')
        print(answer)
        self.send_message(socket, answer)

    @staticmethod
    def send_message(socket: socket, message: dict):
        socket.send(message)

    def start(self):
        # Для проверки ServerVerifier:
        # self.socket.connect()

        while True:
            try:
                client, addr_info = self.socket.accept()
                client_addr, client_port = addr_info

                # Делаем запись в БД о подключении
                # self.db.history_update(client_addr, client_port)
            except OSError as err:
                pass
            else:
                self.clients.append(client)
            finally:
                try:
                    if self.clients:
                        i_cli, o_cli, e_cli = select(self.clients, self.clients, [], 0)
                    else:
                        continue
                except Exception as err:
                    print(f"ОШИБКА: {format_exc()}")

                messages = []  # Обнуляем список сообщений

                for client in i_cli:
                    try:
                        message = self.read_message(client)
                        if message:  # Исключаем пустые строки
                            messages.append(message)
                    except ConnectionResetError:
                        self.clients.remove(client)
                    except json.decoder.JSONDecodeError:
                        self.clients.remove(client)

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
