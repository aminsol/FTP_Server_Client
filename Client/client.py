#!/usr/bin/python3
# This is client.py file
import socket
import os
import sys
import re

# For file transfer
ftp = 3333
# For communicating to server
serverPort = 2222
# For communicating to Client
clientPort = 1111
host = socket.gethostname()


def send(data):
    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name

    # connection to hostname on the port.
    client_socket.connect((host, serverPort))
    # Sending the message
    client_socket.send(data.encode('ascii'))
    # Receiving the response
    respond = client_socket.recv(128)
    client_socket.close()
    return respond.decode('ascii')


def getSize(filename):
    if os.path.isfile(filename):
        filesize = os.stat(filename).st_size
    else:
        filesize = False
    return filesize


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


def upload(uInput):  # pass communication socket hostname and file name
    try:
        fObj = open(uInput, "rb")
        fileSize = getSize(uInput)
        clientCtrSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientCtrSocket.connect((host, ftp))
        print("FTP connection established commncing upload")
        bytesSent = 0
        while bytesSent < int(fileSize):
            fileData = fObj.read()
            if fileData:
                bytesSent += clientCtrSocket.send(fileData)
            print("Sent: " + str(bytesSent) + " / " + str(fileSize).decode())
        print("File upload done...\n")
        fObj.close()
    except FileNotFoundError:
        print("File not found...")
        return "err"
    except ConnectionError:
        print("Error connecting to FTP port \n")
        return "err"


uploadFile = re.compile('upload ([\w\.]+)')
downloadFile = re.compile('download ([\w\.]+)')


command = input("Enter your command: ")
result = ""
if command == "ls":
    result = send("ls")
elif downloadFile.match(command):
    fileName = downloadFile.match(command)[1]
    # Asking server to send us a file
    # if the file exist then server response with file size
    size = send("download " + fileName)
    if size != "err":
        print("Start downloading..")
        result = download(fileName, size)
        print("Download is finished!")
    else:
        # cannot find the file on the server
        print("No such file found on the server!")
elif uploadFile.match(command):
    fileName = uploadFile.match(command)[1]
    fileSize = getSize(fileName)
    if fileSize:
        if send("upload " + fileName + " " + str(fileSize)) == "ok":
            result = upload(fileName)

print(result)
print("Client connection Closed!")
