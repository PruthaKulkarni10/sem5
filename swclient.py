import socket 
import time 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5001))

frame = 0
frame_count = 5

while frame < frame_count:
    print(f"sending frame {frame}")
    client.sendall(f'Frame {frame}.'.encode())

    data = client.recv(1024).decode()

    if f'Ack for frame {frame}' in data:
        print(f'Received data: {data}')
        frame +=1
    
    elif f'Nack for frame {frame}' in data:
        print(f"Received: {data} - Retrying frame {frame}...")
        
    else:
        print(f"Unexpected response: {data}")
    time.sleep(1)

client.close()

