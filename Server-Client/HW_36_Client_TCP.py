import json
import socket

PORT = 8001
SERVER = "192.168.0.102"
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'exit'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER, PORT))


def send(message, key='1'):
    """ функція для відправки повідомлень на серевер"""
    message_key_json = json.dumps({'message': message, 'key': key})
    bytes_ = bytes(message_key_json, 'utf-8')
    message_length = len(bytes_)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    message = message_key_json.encode(FORMAT)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


while (message := input('Введіть повідомлення: ')):
    key = input('Введіть ключ: ')
    send(message, key)
