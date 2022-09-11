import socket


def client(server_id, host):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_id, host))
    connected = True
    while connected:
        client.send(input('your message').encode('utf-8'))
        message = client.recv(1024).decode('utf-8')
        print(f'message for you {message}')
        if message == 'close':
            connected = False
    print('connection is broken')


def main():
    host = 4001
    server_id = '192.168.0.102'
    client(server_id, host)


if __name__ == '__main__':
    main()
