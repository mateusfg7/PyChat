import socket
import os

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(0.2)

messages = []

def MessageLog(msg):
    if msg not in messages:
        messages.append(msg)

while True:
    try:
        while True:
            bytes_message, server_ip = client.recvfrom(2048)
            MessageLog(bytes_message.decode())
    except socket.timeout:
        pass
    os.system('clear')
    for message in messages:
        print(message)
    
    message_to_send = input('> ')
    MessageLog(message_to_send)
    client.sendto(message_to_send.encode(), ('127.0.0.1', 12000))
    
