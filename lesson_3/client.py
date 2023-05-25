import argparse
import json
from time import time
from socket import *
from pprint import pprint
from typing import Union


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
    socket.sendto(message, (address, port))


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


def start(args: argparse.ArgumentParser) -> None:
    """Client for messaging with servers.

    Args:
        args (argparse.ArgumentParser): Server IP and Server Port
    """

    addr, port = args.address, args.port

    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    s.connect((addr, port))

    request = get_presence_msg()  # Формируем presence-сообщение
    send_message_to_server(s, request, addr, port)  # Отправляем серверу
    message = get_responce_from_server(s)  # Получаем ответ от сервера
    response = convert_response(message)  # Преобразуем ответ в dict

    print('Server Response:')  # Читаем ответ
    pprint(response)
    s.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=' > Send message to server.')
    parser.add_argument('address', type=str, help='Server IP.')
    parser.add_argument('port', default=7777, type=int, help='Server Port.')
    args = parser.parse_args()

    start(args)
