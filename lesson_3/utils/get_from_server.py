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

    return json.loads(socket.recv(1000).decode('utf-8'))


def get_from_server(client, addr, port):
    try:
        message = get_responce_from_server(client)  # Получаем ответ от сервера
        LOGGER.info(
            f"Получили ответ от {addr if addr != '' else 'localhost'}:{port} - {message}")
    except Exception:
        LOGGER.critical(
            f"Ошибка при получении данных с сервера {addr if addr != '' else 'localhost'}:{port}")
