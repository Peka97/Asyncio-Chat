import json
import logging
from socket import *

import log.config.client_log_config


LOGGER = logging.getLogger('client')


def get_responce_from_server(socket: socket) -> bytes:
    """Get responce from the server.

    Args:
        socket (socket): Client socket

    Returns:
        bytes: Message from the server
    """

    return socket.recv(1000)


def convert_response(message: bytes) -> dict:
    """Convert message from bytes to dict.

    Args:
        message (bytes): Message from the server

    Returns:
        dict: Dict with response data 
    """

    return json.loads(message.decode('utf-8'))


def get_from_server(client, addr, port):
    try:
        client.connect((addr, port))
        LOGGER.info(
            f"Установлено соединение с {addr if addr != '' else 'localhost'}:{port}")
        message = get_responce_from_server(client)  # Получаем ответ от сервера

        response = convert_response(message)  # Преобразуем ответ в dict
        LOGGER.info(
            f"Получили ответ от {addr if addr != '' else 'localhost'}:{port} - {response}")
    except Exception:
        LOGGER.critical(
            f"Ошибка при получении данных с сервера {addr if addr != '' else 'localhost'}:{port}")
