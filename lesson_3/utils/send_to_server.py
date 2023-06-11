import json
import logging
from time import time
from socket import *
from typing import Union

import log.config.client_log_config
from log.decorator import Log


LOGGER = logging.getLogger('client')


def get_presence_msg() -> dict:
    """Generates a message for the client.

    Returns:
        None
    """

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


@Log(LOGGER)
def send_message_to_server(
        socket: socket,
        message: dict,
        address: Union[str, int],
        port: Union[str, int]
) -> None:
    """Send message to the server.

    Args:
        socket (socket): Client socket
        message (dict): Message to server
        address (Union[str, int]): Server IP
        port (Union[str, int]): Server port
    """
    socket.send(message)


def send_to_server(client, addr, port):
    try:
        client.connect((addr, port))
        LOGGER.info(
            f"Установлено соединение с {addr if addr != '' else 'localhost'}:{port}")

        request = get_presence_msg()  # Формируем presence-сообщение
        send_message_to_server(client, request, addr,
                               port)  # Отправляем серверу
        LOGGER.info(
            f"Отправили сообщение {addr if addr != '' else 'localhost'}:{port}")
    except Exception as err:
        LOGGER.critical(
            f"Ошибка при отправке на сервер {addr if addr != '' else 'localhost'}:{port}")
        LOGGER.critical(err)
