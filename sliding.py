# import random
# import time 

# total_frames = 7
# current_frame = 0

# lost_frames = set()

# while current_frame < total_frames:
    
#     failure = random.randint(0,7)
#     print(f"Sending frame: {current_frame}")

#     if(current_frame == failure):
#         print(f"ack for frame {current_frame} lost")
#         lost_frames.add(failure)

#     else:
#         print(f"ack for frame {current_frame} recieved")

#     current_frame+=1
#     time.sleep(1)

# print("resending frames")
# for frame in lost_frames:
#     print(f"resending frame: {frame}")
#     print(f"ack for frame: {frame} received")

# import random 

# window_size = 3
# frame_count = 8
# frame = 0

# while frame < frame_count:
#     window = []

#     for i in range(window_size):
#         if frame + i < frame_count:
#             window.append(frame+i)

#     print(f"Sending windows: {window}")

#     success = True

#     for current_frame in window:
#         if random.randint(0,7) < 2:
#             print(f"Frame {current_frame} is lost")
#             success = False

#         else:
#             print(f"ack for frame {current_frame} is recieved")

#     if success:
#         frame+=window_size
#     else:
#         print(f"resending from frames {frame}")

# choice = int(input("enter:\n choice 1: error detection\nchoice 2: find transmitted bit stream"))

# def xorbit(dividend, divisor):
#     x = ''
#     if(dividend[0]=='1'):
#         for i in range(len(dividend)):
#             x+=str((int(dividend[i]+divisor[i]))%2)

#     else:
#         x = dividend
    
#     return x [1:]

# if choice == 1:
#     data = input("enter trans msg")
#     divisor = input("enter divisor")
#     new = data + '0'*(len(divisor)-1)
#     dividend = new[0:len(divisor)]
#     i = len(divisor)
#     while i < len(new):
#         prod = xorbit(dividend, divisor)
#         dividend = prod + new[i]
#         i+=1
#     remiander = xorbit(dividend, divisor)
#     if remiander == 0:
#         print("no error")
#     else:
#         print("error")

# elif(choice == 2):
#     data = input("enter trans msg")
#     divisor = input("enter divisor")
#     new = data + '0'*(len(divisor)-1)
#     dividend = new[0:len(divisor)]
#     i = len(divisor)
#     while i < len(new):
#         prod = xorbit(dividend, divisor)
#         dividend = prod + new[i]
#         i+=1
#     remiander = xorbit(dividend, divisor)
#     print(f"{data}{remiander}")

# choice = int(input("Enter\n1:error detection\n2:transmitted bit stream"))

# def xorbit(dividend, divisor):
#     x = ''
#     if (dividend[0] == 1):
#         for i in range(len(dividend)):
#             x += str((int(dividend[i] + divisor[i]))%2)

#     else:
#         x += dividend

#     return x[1:]

# if choice == 1:
#     data = input("enter transmitted msg")
#     divisor = input("enter divisor")
#     new = data + '0'*(len(divisor)-1)
#     dividend = new[0:len(divisor)]
#     i = len(divisor)
#     while i<len(dividend):
#         prod = xorbit(dividend, divisor)
#         dividend = prod + new[i]
#         i+=1
#     remainder = xorbit(dividend, divisor)
#     if(remainder==0):
#         print("no error")
#     else:
#         print("error")

# def generate_hamming(data_bits, parity_type):
#     n = len(data_bits)
#     m = 0
#     while (2**m <m+n+1):
#         m+=1

#     hamming = [None] * (m+n)
#     j=0

#     for i in range(len(hamming)):
#         if (i+1) & i:
#             hamming[i] = int(data_bits[j])
#             j+=1

#     for i in range(m):
#         parity_index = (2**i) - 1
#         parity_sum = sum(hamming[k] for k in range(len(hamming)) if (k+1) & (parity_index+1) and hamming[k] is not None)
#         hamming[parity_index] = 0 if parity_sum % 2 == (0 if parity_type == 'even' else 1) else 1

#     return ''.join(map(str,hamming))

# def detect_and_correct(data, parity_type):
#     hamming = list(map(int, data))
#     n = len(hamming)
#     m = 0
#     while (2**m) < (m+n+1):
#         m+=1
    
#     error_pos = 0
#     for i in range(m):
#         parity_index = (2**i)-1
#         parity_sum = sum(hamming[k] for k in range(n) if (k+1) & (parity_index+1))
#         if parity_sum % 2 != (0 if parity_type == "even" else 1):
#             error_pos += 2**i

#     if error_pos:
#         hamming[error_pos-1]^=1

#     return ''.join(map(str, hamming)), error_pos



# data_bits = input("enter data")
# parity_type = input("enter parity type")
# if parity_type in ["even", "odd"]:
#     hamming_code = generate_hamming(data_bits, parity_type)
#     print("Generated hamming code: ", hamming_code)

#     transmitted = input("enter transmitted hamming code")
#     corrected_code, error_pos = detect_and_correct(transmitted, parity_type)

#     if error_pos:
#         print(f"error corrected and detected at {error_pos}")
#     else:
#         print("no error")

#     print()

# import socket
# import threading
# import time

# MAX_SIZE = 5 
# LEAK_RATE = 0.5
# HOST = '0.0.0.0'
# PORT = 5001

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((HOST, PORT))

# server_socket.listen()

# # Accept a client connection
# conn, addr = server_socket.accept()
# received_data = []

# def leaky():
#     while True:
#         time.sleep(1 / LEAK_RATE)  
#         if received_data:
#             leaked_data = received_data.pop(0)  
#             print(f"Leaked data: {leaked_data}")
#         else:
#             print("Bucket is empty, no data to leak.")


# def addInQueue():
#     with conn:
#         while True:
#             data = conn.recv(1024)
#             if not data or data.decode() == "end":
#                 if len(received_data)>0:
#                      print(f"Remaining data: {received_data}")

#                 print("Client has ended communication")
#                 break

# # Run the leaky bucket function in a separate thread
# leaky_thread = threading.Thread(target=leaky, daemon=True)
# leaky_thread.start()
# addInQueue()

# # Close the server socket
# server_socket.close()

# import socket
# import time
# import threading

# HOST='0.0.0.0'
# PORT=5000

# MAX_SIZE=5

# server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server_socket.bind((HOST,PORT))

# server_socket.listen()
# conn,addr=server_socket.accept()

# tokens=[]
# received_data=[]

# def leaky():
#     while True:
#         time.sleep(3)
#         if received_data:
#             removed_data=received_data.pop(0)
#             print(f"Removed data :{removed_data}")
#         else:
#             print("Bucket is empty")

# def handleTokens():
#     while True:
#         if len(tokens)<MAX_SIZE:
#             tokens.append('*')
#             print(f"Token bucket looks like :{tokens}")
#         else:
#             print("Token bucket is full")
#         time.sleep(1)

# def handleData():
#     with conn:
#         while True:
#             data=conn.recv(1024).decode()
#             if not data or data=='end':
#                 if len(tokens)>0:
#                     print(f"Tokens left:{tokens}")
#                 print("Connection ended by client")
#                 break

#             if len(tokens)>0:
#                 tokens.pop(0)
#                 print(f"Data:{data} added to bucket")
#                 conn.send(data.encode())
#                 received_data.append(data)
#                 print(f"Bucket contains:{received_data}")

#             else:
#                 print("No tokens discarding data")
#                 message="No tokens available"
#                 conn.send(message.encode())

# token_thread=threading.Thread(target=handleTokens,daemon=True)
# token_thread.start()

# leaky_thread=threading.Thread(target=leaky,daemon=True)
# leaky_thread.start()

# handleData()

# server_socket.close()

# choice = input("enter:\1:nerror detection\n2:error correction")

# def xorbit(dividend, divisor):
#     x = ''
#     if(dividend[0]==1):
#         for i in range(len(dividend)):
#             dividend+=str((int(dividend) + int(divisor))%2)
#     else:
#         x = dividend
#     return x[1:]

# if (choice==1):
#     data = input("enter data ")
#     divisor = input("enter divisor")
#     new = data + '0'*(len(divisor)-1)
#     dividend = new[0: len(divisor)]
#     i = len(divisor)

#     while i<len(new):
#         prod = xorbit(dividend, divisor)
#         dividend = prod + new[i]
#         i+=1

#     remainder = xorbit(dividend, divisor)
#     if int(remainder)==0:
#         print("error")
#     else:
#         print("no error")        

# choice = int(input("enter 1: ed 2: ec"))

# def xorbit(dividend, divisor):
#     x = ''
#     if (dividend[0]==1):
#         for i in range(len(dividend)):
#             x += str((int(dividend[i])+int(divisor[i]))%2)
#     else:
#         x = dividend
#     return x[1:]

# if (choice==1):
#     data = input("enter data")
#     divisor = input("enter divsor")
#     new = data + '0'*(len(divisor)-1)
#     dividend = new[0:len(divisor)]
#     i = len(divisor)

#     while i<len(new):
#         prod = xorbit(dividend,divisor)
#         dividend = prod + new[i]
#         i+=1

#     remainder = xorbit(dividend, divisor)
#     if int(remainder)==0:
#         print("ne")
#     else:
#         print("e")

# else:
#     data = input("enter data")
#     divisor = input("enter divsor")
#     new = data + '0'*(len(divisor)-1)
#     dividend = new[0:len(divisor)]
#     i = len(divisor)

#     while i<len(new):
#         prod = xorbit(dividend,divisor)
#         dividend = prod + new[i]
#         i+=1

#     remainder = xorbit(dividend, divisor)
#     print(f"corrected data: {data}{remainder}")

# def generate_hamming(data_bits, parity_type):
#     n = len(data_bits)
#     m=0

#     while (2 ** m ) < (m+n+1):
#         m+=1
#     j=0
#     hamming = [None] * (m+n)

#     for i in range(len(hamming)):
#         if (i+1) & i:
#             hamming[i] = int(data_bits[j])
#             j+=1

#     for i in range(m):
#         parity_index = (2**i) - 1 
#         parity_sum = sum(hamming[k] for k in range(len(hamming)) if (k+1) & (parity_index+1) and hamming[k] is not None)
#         hamming[parity_index] = 0 if parity_sum%2 == (0 if parity_type=='even' else 1)else 1

#     return ''.join(map(str, hamming))

# def detect_and_correct(data, parity_type):
#     hamming = list(map(int,data))
#     n = len(hamming)

#     m=0

#     while (2 ** m ) < n:
#         m+=1
#     j=0

#     error_pos = 0

#     for i in range(m):
#         parity_index = (2**i) - 1 
#         parity_sum = sum(hamming[k] for k in range(n) if (k+1) & (parity_index+1))
#         if parity_sum%2 != (0 if parity_type=='even'else 1):
#             error_pos += 2**i

#     if error_pos:
#         hamming[error_pos-1] ^=1

#     return ''.join(map(str, hamming)), error_pos

# data_bits = input("enter data bits")
# parity_type = input("enter even or odd")

# hamming_code = generate_hamming(data_bits, parity_type)
# print(f"generated hamming code: {hamming_code}")

# transmitted_code = input("enter transmitted code:")

# corrected_code, error_pos = detect_and_correct(transmitted_code, parity_type)
# print(f"error at pos: {error_pos}, corrected code: {corrected_code}")

# import random 
# import time

# window_size = 3
# frame_count = 8
# frame = 0

# while frame<frame_count:
#     window = []
#     for i in range(window_size):
#         if frame + i<frame_count:
#             window.append(frame+i)

#     print(f"sending frames in window: {window}")

#     success = True
#     for currentframe in window:
#         if random.randint(0,7) < 2:
#             print(f"ack for frame {currentframe} is lost")
#             success = False
#             break

#         else:
#             print(f"ack for frame {currentframe} recieved")

#     if success:
#         frame+=window_size
#     else:
#         print(f"resending from frame: {currentframe}")
#         time.sleep(1)


    
# import random 

# window_size = 3
# frame = 0
# frame_count = 8

# while frame < frame_count:
#     window = []

#     for i in range(window_size):
#         if frame + i<frame_count:
#             window.append(frame+i)

#     print(f"sending window {window}")

#     success = True
#     for currentframe in window:
#         if random.randint(0,7)<2:
#             print(f"ack for frame {currentframe} is lost")
#             success = False
#             break

#         else:
#             print(f"ack for {currentframe} received")

#     if success:
#         frame+=window_size
        
#     else:
#         print(f"resending from frame {currentframe}")

# import random 
# import time 

# frame = 0
# frame_count = 8

# lost_frame = set()

# while frame<frame_count:
#     print(f"sending frame {frame}")
#     if frame == random.randint(0,7):
#         print(f"ack for frame {frame} is lost")
#         lost_frame.add(frame)
#     else:
#         print(f"ack for frame {frame} received")

#     frame+=1
#     time.sleep(1)

# print("\nResending lost frames")
# for frame in lost_frame:
#     print(f"ack for lost frame {frame} received")

# data = input("enter data ")

# i = count = 0

# while i < len(data):
#     print(data[i], end = '')

#     if(data[i]=='1'):
#         count+=1
#         if(count==5):
#             print(0, end='')
#             count = 0
#     else:
#         count = 0

#     i+=1
