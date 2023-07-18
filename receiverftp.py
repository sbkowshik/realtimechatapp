# This file will be used for recieving files over socket connection.
import os
import socket
import time

host = input("Host Name: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Trying to connect to socket.
try:
    sock.connect((host, 22222))
    print("Connected Successfully")
except:
    print("Unable to connect")
    exit(0)

# Send file details.
file_name = sock.recv(1024).decode()
print(file_name)
file_size = sock.recv(1024).decode()
print(file_size)


# Closing the socket.
sock.close()