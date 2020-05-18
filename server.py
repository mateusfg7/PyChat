import socket
import os
from datetime import datetime

# define o tipo de socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 12000))  # onde vai ser usado: (host, port)

clients = []
messages = []

def MessageLog(msg):
    if msg not in messages:
        messages.append(msg)

while True:
    bytes_message, client_ip = server.recvfrom(2048)  # responsta do cliente

    if client_ip not in clients:
        clients.append(client_ip)
    MessageLog(bytes_message.decode())

    for client in clients:
        os.system('clear')
        print(f'destination: {client}\n')
        for message in messages:
            now = datetime.now()
            print(f'{now.hour}:{now.minute}:{now.second} > {message}')
            server.sendto(message.encode(), client)
