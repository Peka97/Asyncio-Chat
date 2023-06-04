import json
import argparse
import logging
from time import time
from socket import *
from typing import Union

import log.config.server_log_config
from log.decorator import Log


LOGGER = logging.getLogger('server')


@Log(LOGGER)
def get_message_from_client(client: socket) -> str:
    """Gets and converts the message to string form

    Args:
        client (socket): Client socket.

    Returns:
        Str: Message from client.
    """

    return client.recv(1000).decode('utf-8')


def get_responce_to_client(
    message: str,
    address: Union[str, int],
    port: Union[str, int]
) -> dict:
    """Generates a response based on the passed message.

    Args:
        message (str): Message from client.
        address (Union[str, int]): IP of client.
        port (Union[str, int]): Port of client.

    Returns:
        dict: Response.
    """

    try:
        json.loads(message)
        response = {
            "response": 200,
            "time": time(),
        }
    except json.decoder.JSONDecodeError:
        LOGGER.error(
            f'Не удалось распарсить JSON от {address}:{port}')
        response = {
            "response": 400,
            "time": time(),
            "alert": "Bad Request"
        }
    except Exception:
        LOGGER.critical(
            f'Не удалось прочесть JSON от {address}:{port}.')
        response = {
            "response": 500,
            "time": time(),
            "alert": "Server Error"
        }

    return response


def send_to_client(
    client: socket,
    address: Union[str, int],
    port: Union[str, int],
    message: dict,
) -> None:
    """Sends a message to the client.

    Args:
        client (socket): Socket of client.
        address (Union[str, int]): IP of client.
        port (Union[str, int]): Port of client.
        message (dict): Message from server.
    """

    client.sendto(json.dumps(message).encode('utf-8'),
                  (address, port))
    LOGGER.info(f'Отправка сообщения клиенту {address}:{port}')


def start(args: argparse.ArgumentParser) -> None:
    """Server for messaging with clients.

    Args:
        args (argparse.ArgumentParser): Port to work and IP to listening.
    """

    port, addr = args.p, args.a
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((addr, port))
    s.listen(5)

    while True:
        client, addr_info = s.accept()
        client_addr, client_port = addr_info
        LOGGER.info(f'Подключение клиента: {client_addr}:{client_port}')

        message = get_message_from_client(client)  # Принимаем сообщение
        response = get_responce_to_client(
            message, client_addr, client_port
        )  # Формируем ответ клиенту
        send_to_client(client, client_addr, client_port,
                       response)  # Отправляем ответ клиенту


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=' > Get messages from clients.')
    parser.add_argument('-p', default=7777, type=int, help='Server Port.')
    parser.add_argument('-a', default='', type=str,
                        help='Server IP to listening.')
    args = parser.parse_args()

    start(args)
