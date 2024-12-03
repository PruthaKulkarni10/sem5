import socket, time, threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5001))
server.listen()

conn, addr = server.accept()
leak_rate = 0.5
max_size = 5

received_data = []
tokens = []

def leaky():
    time.sleep(3)
    if received_data:
        leaked_data = received_data.pop()
        print(f"Leaked data: {leaked_data}")
    else:
        print('bucket empty')

def handle_tokens():
    while True:
        if len(tokens)<max_size:
            tokens.append('*')
        else:
            print('bucket full')
        time.sleep(1)

def handle_data():
    with conn:
        while True:
             data = conn.recv(1024).decode()

             if data == 'end':
                if len(received_data)>0:
                     print(f'remaining data: {received_data}')
                print('connection ends')
                break
             
             if len(tokens)>0:
                 tokens.pop(0)
                 received_data.append(data)
                 print(f"received data: {data}")

             else:
                 print("nothing to pop")

token_thread = threading.Thread(target=handle_tokens, daemon=True)
token_thread.start()

leaky_thread = threading.Thread(target=leaky, daemon=True)
leaky_thread.start()


handle_data()

server.close()