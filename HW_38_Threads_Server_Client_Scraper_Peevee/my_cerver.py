import socket
import threading


def server(server_id, host):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_id, host))
    server.listen()
    print('server listening')
    while True:
        connection, client = server.accept()
        thread = threading.Thread(target=handling_con,
                                  args=(connection, client))
        thread.start()
        print(f'amount connections {threading.active_count() - 1}')


def handling_con(connect, client):
    connected = True
    print(f'Handling client {client}')
    while connected:
        message = connect.recv(1024).decode('utf-8')
        print(f'message for you {message}')
        if message == 'close':
            connected = False
            connect.send(message.encode('utf-8'))
        else:
            connect.send(message.encode('utf-8'))
        print(f'your message {message}')
    connect.close()


def main():
    host = 4001
    server_id = '192.168.0.102'
    server(server_id, host)


if __name__ == '__main__':
    main()


