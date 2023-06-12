from socket import socket


def read_message(socket: socket):
    return socket.recv(1024).decode('utf-8')


def send_message(socket: socket, message: str):
    socket.send(message.encode('utf-8'))
