import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5001))

while True:
    clientMsg = input("Client: ")
    client.sendall(clientMsg.encode())

    if clientMsg == 'end':
        print("commuinication ended")
        break

client.close()