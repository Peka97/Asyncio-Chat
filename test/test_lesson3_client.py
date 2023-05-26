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
        client, _ = self.client.accept()
        self.server.sendto(b'Test string', (self.addr, self.port))

        result = get_responce_from_server(client)
        self.assertAlmostEqual(result, 'Test string')

    def test_convert_response(self):
        message = json.dumps({
            "response": 200,
            "time": time(),
        }).encode('utf-8')
        r = convert_response(message)

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


if __name__ == '__main__':
    unittest.main()
