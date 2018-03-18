#!/usr/bin/python3
# This is server.py file
import socket
import re

# The ports on which to listen

# For file transfer
FTP = 3333
# For communicating to server
serverPort = 2222
# For communicating to Client
clientPort = 1111



def download(filename):
    return filename

def upload(filename):
    return filename

def ls():
    return "<directories>"


# Create a TCP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
responseSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
serverSocket.bind(('',serverPort))
host = socket.gethostname()


# Start listening for incoming connections
serverSocket.listen(serverPort)

print("The server is ready to receive")
uploadfile = re.compile('upload (\w+\.\w+)')
downloadfile = re.compile('download (\w+\.\w+)')
# The buffer to storetherreceived data
data = ""
response = ""
# Forever accept incoming connections
while True:
    # Accept a connection; get client’s socket
    connectionSocket,addr = serverSocket.accept()
    # Receive whatever the newly connected client has to send
    data = connectionSocket.recv(40).decode('ascii')
    if data == "ls":
        print(ls())
    elif downloadfile.match(data):
        print(download(downloadfile.match(data)[1]))
    elif uploadfile.match(data):
        print(upload(uploadfile.match(data)[1]))
    else:
        print("err")

    # Close the socket
    connectionSocket.close()