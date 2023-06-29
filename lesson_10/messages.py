import json
from time import time


class Message:
    def __init__(self) -> None:
        pass

    @staticmethod
    def auth(username: str, password: str) -> bytes:
        message = {
            'action': 'auth',
            'time': time(),
            'username': username,
            'password': password

        }
        return json.dumps(message, indent=4).encode('utf-8')

    @staticmethod
    def send_message(send_from: str, text: str, send_to: str):
        pass

    @staticmethod
    def get_contacts(username: str) -> bytes:
        message = {
            'action': 'get_contacts',
            'time': time(),
            'username': username
        }
        return json.dumps(message, indent=4).encode('utf-8')

    @staticmethod
    def send_contacts(friends: list) -> bytes:
        message = {
            "response": "202",
            "alert": friends
        }
        return json.dumps(message).encode('utf-8')

    @staticmethod
    def add_contact(username: str, contact_id: str) -> bytes:
        message = {
            "action": "add_contact",
            "time": time(),
            "username": username,
            "contact_id": contact_id,
        }
        return json.dumps(message).encode('utf-8')

    @staticmethod
    def del_contact(username: str, contact_id: str) -> bytes:
        message = {
            "action": "del_contact",
            "time": time(),
            "username": username,
            "contact_id": contact_id,
        }
        return json.dumps(message).encode('utf-8')
