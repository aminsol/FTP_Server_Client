#!/usr/bin/python3
# This is server.py file
import socket
import os
import re

# The ports on which to listen

# For file transfer
FTP = 3333
# For communicating to server
serverPort = 2222
# For communicating to Client
clientPort = 1111


def getsize(filename):
    if os.path.isfile(filename):
        size = os.stat(filename).st_size
    else:
        size = False
    return size

def download(filename, filesize):
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
uploadfile = re.compile('upload ([\w\.]+) (\d+)')
downloadfile = re.compile('download ([\w\.]+)')
# The buffer to storetherreceived data
data = ""
response = ""
# Forever accept incoming connections
while True:
    # Accept a connection; get client’s socket
    connectionSocket,addr = serverSocket.accept()
    # Receive whatever the newly connected client has to send
    data = connectionSocket.recv(128).decode('ascii')
    if data == "ls":
        connectionSocket.send(ls().encode('ascii'))
    elif downloadfile.match(data):
        fileName = downloadfile.match(data)[1]
        fileSize = str(getsize(fileName))
        connectionSocket.send(fileSize.encode('ascii'))
        upload(fileName)
    elif uploadfile.match(data):
        fileName = uploadfile.match(data)[1]
        fileSize = int(uploadfile.match(data)[2])
        connectionSocket.send("ok".encode('ascii'))
        download(fileName, fileSize)
    else:
        connectionSocket.send("err".encode('ascii'))
        print("err")
# Close the socket
connectionSocket.close()