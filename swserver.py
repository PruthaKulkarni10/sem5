import socket
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5001))
server.listen(1)

client, addr = server.accept()

frame = 0
frame_count = 5

while frame < frame_count:
    data = client.recv(1024).decode()
    print(f"Received: {data}")
    ack = random.choice([True, False])

    if ack:
        client.sendall(f"Ack for frame {frame}".encode())
        print(f"Ack for frame {frame} sent")
        frame+=1

    else:
        client.sendall(f"Nack for frame {frame}".encode())
        print(f"nack for frame {frame} send ")

client.close()
server.close()