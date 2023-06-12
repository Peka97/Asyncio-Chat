from socket import *
from select import select

from utils import send_message, read_message


def mainloop():
    ADDR = ''
    PORT = 7777

    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ADDR, PORT))
    server.listen(5)
    server.settimeout(1)

    clients = []

    while True:
        try:
            client, addr_info = server.accept()
            client_addr, client_port = addr_info
        except OSError as err:
            pass
        else:
            clients.append(client)
        finally:
            try:
                i_cli, o_cli, e_cli = select(clients, clients, [], 0)
            except Exception:
                pass

            messages = []  # Обнуляем список сообщений

            for client in i_cli:
                message = read_message(client)
                if message:  # Исключаем пустые строки
                    messages.append(message)

            if messages:  # Проверяем есть ли сообщения
                for message in messages:
                    for client in o_cli:
                        try:
                            send_message(client, message)
                        except Exception:
                            clients.remove(client)


if __name__ == '__main__':
    mainloop()
