#!/usr/bin/python3
# This is client.py file
import socket
import os
import re

# For file transfer
FTP = 3333
# For communicating to server
serverPort = 2222
# For communicating to Client
clientPort = 1111


def send(data):
    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = socket.gethostname()

    # connection to hostname on the port.
    client_socket.connect((host, serverPort))
    # Sending the message
    client_socket.send(data.encode('ascii'))
    # Receiving the response
    respond = client_socket.recv(128)
    client_socket.close()
    return respond


def getsize(filename):
    if os.path.isfile(filename):
        size = os.stat(filename).st_size
    else:
        size = False
    return size


def download(filename, size):
    return filename


def upload(filename):
    return filename


def ls():
    return send("ls".encode('ascii'))


uploadFile = re.compile('upload ([\w\.]+)')
downloadFile = re.compile('download ([\w\.]+)')


command = input("Enter your command: ")
result = ""
if command == "ls":
    result = ls()
elif downloadFile.match(command):
    fileName = downloadFile.match(command)[1]
    # Asking server to send us a file
    # if the file exist then server response with file size
    size = send("download " + fileName)
    if size != "err":
        result = download(fileName, size)
elif uploadFile.match(command):
    fileName = uploadFile.match(command)[1]
    fileSize = getsize(fileName)
    if fileSize:
        send("upload " + fileName + " " + str(fileSize))
        result = upload(fileName)
print("Client connection Closed!")