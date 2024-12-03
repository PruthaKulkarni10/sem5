import socket, threading, time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5001))
server.listen()

conn, addr = server.accept()

max_size = 5
received_data = []
tokens = []

def leaky():
    while True:
        time.sleep(3)
        if received_data:
            removed_data = received_data.pop(0)
            print(f"removed data: {removed_data}")
        else:
            print("no data")

def handle_tokens():
    while True:
        if len(tokens) < max_size:
            tokens.append('*')
        else:
            print('token is full')
        time.sleep(1)

def handle_data():
    with conn:
        while True:
            data = conn.recv(1024).decode()
            if not data or data == 'end':
                print("connection ended")
                break

            if len(tokens)>0:
                tokens.pop(0)
                print(f"data recieved: {data}")
                received_data.append(data)
                print(f"bucket contains: {received_data}")


token_thread = threading.Thread(target=handle_tokens, daemon=True)
token_thread.start()

leaky_thread = threading.Thread(target = leaky, daemon=True)
leaky_thread.start()

handle_data()
server.close()
