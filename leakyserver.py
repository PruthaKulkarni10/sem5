import socket, threading, time 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5001))
server.listen()

conn, addr = server.accept()

leak_rate = 0.5
received_data = []

def leaky():
    while True:
        time.sleep(1/leak_rate)
        if received_data:
            leaked_data = received_data.pop(0)
            print(f"Leaked data: {leaked_data}")
        else:
            print("nothing to pop")


def addInQueue():
    with conn:
        while True:
            data = conn.recv(1024)
            if not data or data.decode() == 'end':
                if len(received_data)>0:
                    print(f"remaining data: {received_data}")
                print("connection ends")
                break

            if len(received_data) < 5:
                received_data.append(data.decode())
                print(f"received_data: {received_data}")
            else:
                print("queue is full")

leaky_thread = threading.Thread(target=leaky, daemon=True)
leaky_thread.start()
addInQueue()

server.close()

