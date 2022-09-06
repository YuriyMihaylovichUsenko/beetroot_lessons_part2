import json
import socket
import threading

PORT = 8001  # ПОРТ ЩО МИ ВІДКРИЄМО ДЛЯ РОБОТИ
SERVER = socket.gethostbyname(socket.gethostname())

ADDRESS = (SERVER, PORT)

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'exit'

# Створюємо сервер, додаємо сім'ю і тип серверу
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDRESS)


def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


def handle_client(connection, address):
    # ця функція буде використовуватися для обробки зв'язку з сервером клієнту
    print(f'NEW CONNECTION - {address}')
    connected = True
    while connected:
        # recv(кількість байтів що отримає клієнт)
        # Але ми не можемо знати завчасно скільки отримаємо
        # тому варто створити хедер
        # раз ми не знаємо розмір повідомлення, що буде відправлено на сервер
        # то ми будемо спочатку відправляти розмір повідомлення.
        # в recv будемо вказувати хедер, а потім
        # будемо відправляти саме повідомлення
        message_length = connection.recv(HEADER).decode(FORMAT)
        if message_length:  # later after client first try
            message_length = int(message_length)
            message_json = connection.recv(message_length).decode(FORMAT)
            message_dict = json.loads(message_json)
            key = int(message_dict.get('key', 1))
            message = message_dict.get('message', 'uppps')

            # далі маємо потурбуватися, щоб з'єднання було закрито
            if message == DISCONNECT_MESSAGE:
                connected = False

        print(f'[{address}] - {message}')
        print(key)
        # Тепер сервер відправляє закодоване повідомлення
        connection.send(
            f'Your encrypt message {encrypt(message, key)} '.encode(FORMAT)
        )
    connection.close()


def start():
    server.listen()
    print(f'SERVER LISTEN ON: {SERVER}')
    while True:
        # connettion - це об'єкт сокет
        connection, address = server.accept()
        # handle_client(connection, address)  # спочатку запустити
        # в одному потоці
        thread = threading.Thread(
            target=handle_client, args=(connection, address)
        )
        thread.start()
        print(f'ACTIVE CONNECTIONS {threading.active_count() - 1}')


print('Server started')
start()
