import socket 
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5001))

while True:
    data = input("client: ")
    client.sendall(data.encode())

    if data == 'end':
        print("communication ended")
        break

client.close()