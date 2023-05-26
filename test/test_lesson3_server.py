import unittest
from time import time
from socket import *
from lesson_3.server import get_message_from_client, get_responce_to_client


class TestServerFunction(unittest.TestCase):
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

    def test_get_message_from_client(self):
        # Подготовка
        client, _ = self.server.accept()
        self.client.sendto(b'Test string', (self.addr, self.port))

        # Проверка
        result = get_message_from_client(client)
        self.assertAlmostEqual(result, 'Test string')

    def test_get_responce_to_client_OK(self):
        message = '{"field": "data"}'
        r = get_responce_to_client(message)

        # Ввиду того, что возвращается словарь, проверяю ключевые поля
        self.assertAlmostEqual(
            r['response'],
            200
        )
        self.assertAlmostEqual(
            r['time'],
            time(),
            1
        )

    def test_get_responce_to_client_bad_request(self):
        message = "some data"
        r = get_responce_to_client(message)
        self.assertAlmostEqual(
            r['response'],
            400
        )
        self.assertAlmostEqual(
            r['time'],
            time(),
            1
        )
        self.assertAlmostEqual(
            r['alert'],
            "Bad Request"
        )

    def test_get_responce_to_client_server_error(self):
        message = 1234
        r = get_responce_to_client(message)
        self.assertAlmostEqual(
            r['response'],
            500
        )
        self.assertAlmostEqual(
            r['time'],
            time(),
            1
        )
        self.assertAlmostEqual(
            r['alert'],
            "Server Error"
        )


if __name__ == '__main__':
    unittest.main()
