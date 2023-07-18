import socket
import threading
import queue
import random
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.bind(("localhost",random.randint(8000,9000)))
print("Client 1 ")
name=input("Enter Name 1 : ")
print(" ")
def recieve():
    while True:
        try:
            message,_=client.recvfrom(1024)
            print(message.decode())
        except:
            pass

t=threading.Thread(target=recieve)
t.start()
client.sendto(f"SIGN_TAG:{name}".encode(),("localhost",9999))
while True:
    message=input("")
    if message=="!q":
        exit()
    else:
        client.sendto(f"{name}:{message}".encode(),("localhost",9999))