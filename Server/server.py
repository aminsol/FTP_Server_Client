#!/usr/bin/python3
# This is server.py file
import socket
import os
import re

# The ports on which to listen

# For file transfer
ftp = 3333
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
    # create TCP transfer socket on client to use for connecting to remote
    # server. Indicate the server's remote listening port
    clientSocket_transf = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = socket.gethostname()

    # open the TCP transfer connection
    clientSocket_transf.connect((host, ftp))

    # connection prompt
    print("TCP transfer connected. | Server: %s, Port: %d" % (host, ftp))

    # get the data back from the server
    filedata = clientSocket_transf.recv(1024)

    # creat a file named "filename" and ready to write binary data to the file
    filehandler = open(filename, 'wb')

    # store amount of data being recieved
    totalRecv = len(filedata)

    # write the data to the file
    filehandler.write(filedata)

    print("file size: %d " % filesize)
    print("Total Recieved: %d " % totalRecv)

    # loop to read in entire file
    while totalRecv < filesize:
        filedata = clientSocket_transf.recv(1024)
        totalRecv = totalRecv + len(filedata)
        filehandler.write(filedata)
        print("Total Recieved: %d " % totalRecv)

    # close the file
    filehandler.close()

    # close the TCP transfer connection
    return clientSocket_transf.close()


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