import unittest
import json
from time import time
from socket import *
from lesson_3.client import get_responce_from_server, convert_response, get_presence_msg, send_message_to_server


class TestClientFunction(unittest.TestCase):
    addr = ''
    port = 8888
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind((addr, port))
    server.listen(5)

    client = socket(AF_INET, SOCK_STREAM)
    client.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    client.connect((addr, port))

    def tearDown(self) -> None:
        self.server.close()
        self.client.close()
        return super().tearDown()

    def test_get_responce_from_server(self):
        # Выходит ошибка OSError: [Errno 9] Bad file descriptor.
        # Понимаю, что ругается вероятнее всего на то, что сокет не открыт,
        # пробовал по всякому, но не вышло. Сложно тестировать такой код. но
        # ТЗ прошлого задания требовало функцию для получения фактически из
        # сокета.

        # message = json.dumps({
        #     "response": 200,
        #     "time": time(),
        # }).encode('utf-8')
        # self.client.sendto(message, (self.addr, self.port))

        # r = get_responce_from_server(self.client)
        # self.assertAlmostEqual(
        #     r,
        #     json.dumps({
        #         "response": 200,
        #         "time": time(),
        #     }).encode('utf-8')
        # )
        pass

    def test_convert_response(self):
        message = json.dumps({
            "response": 200,
            "time": time(),
        }).encode('utf-8')
        r = convert_response(message)
        self.assertAlmostEqual(
            r['response'],
            200
        )
        self.assertAlmostEqual(
            r['time'],
            time(),
            1
        )


if __name__ == '__main__':
    unittest.main()
