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
    message = message.encode(FORMAT)
    key = key.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    send_length_key = str(len(key)).encode(FORMAT)
    client.send(send_length_key)
    client.send(key)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


while (message := input('Введіть повідомлення: ')) != DISCONNECT_MESSAGE:
    key = input('Введіть ключ: ')
    send(message, key)
