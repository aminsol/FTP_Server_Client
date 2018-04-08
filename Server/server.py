#!/usr/bin/python3
# This is server.py file
import socket
import os
import sys
import re

# The ports on which to listen

# For file transfer
ftp = 3333
# For communicating to server
#serverPort = 2222
# For communicating to Client
clientPort = 1111

# Check is command from client is: "python3 <serverFilename> <portNumber>"
# Exit if not
if len(sys.argv) == 2:
    serverFile = sys.argv[0]
    serverPort = int(sys.argv[1])
    
    print("Server Port: %d" % serverPort )
else:
    print("Invalid argument(s): usage 'python3 server.py <port number>'")
    sys.exit()

def getsize(filename):
    if os.path.isfile(filename):
        size = os.stat(filename).st_size
    else:
        size = False
    return size


def download(filename, filesize):
    filesize = int(filesize)
    # create TCP transfer socket on client to use for connecting to remote
    # server. Indicate the server's remote listening port
    clientSocket_transf = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = socket.gethostname()

    # open the TCP transfer connection
    clientSocket_transf.bind(('', ftp))
    # Start listening for incoming connections
    clientSocket_transf.listen(ftp)
    connectionSocket,addr = clientSocket_transf.accept()
    # get the data back from the server
    filedata = connectionSocket.recv(1024)

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
        filedata = connectionSocket.recv(1024)
        totalRecv = totalRecv + len(filedata)
        filehandler.write(filedata)
        print("Total Recieved: %d " % totalRecv)

    # close the file
    filehandler.close()
    print("Upload from client complete...")

    # close the TCP transfer connection
    return clientSocket_transf.close()


def upload(filename):  # pass communication socket hostname and file name
    try:
        fObj = open(filename, "rb")
        fileSize = getsize(filename)
        clientCtrSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientCtrSocket.connect((host, ftp))
        print("FTP connection established commncing upload")
        bytesSent = 0
        while bytesSent < int(fileSize):
            fileData = fObj.read()
            if fileData:
                bytesSent += clientCtrSocket.send(fileData)
        print("File " + filename + " upload done...\n")
        fObj.close()
    except FileNotFoundError:
        print("File not found...")
        return "err"
    except ConnectionError:
        print("Error connecting to FTP port \n")
        return "err"


def ls(path):
    if os.path.isdir(path):
        return "\n".join(os.listdir(path))
    else:
        return "Not such directory exist!"

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
lscommand = re.compile('^ls ([\w\.\\\/]*)$|^ls$')
# The buffer to storetherreceived data
data = ""
response = ""
# Forever accept incoming connections
while True:
    # Accept a connection; get client’s socket
    connectionSocket,addr = serverSocket.accept()
    print("Established Connection with: " + str(addr))
    # Receive whatever the newly connected client has to send
    data = connectionSocket.recv(128).decode('ascii').strip()
    
    if lscommand.match(data):
        print("MSG: Recived ls command")
        connectionSocket.send(ls(".").encode('ascii'))
    elif downloadfile.match(data):
        data = data.split(" ")
        print("MSG: Recived download command")
        fileName = data[1]
        fileSize = str(getsize(fileName))
        if fileSize == "False":
           print("File requested not found sending err msg...")
           connectionSocket.send("err".encode('ascii'))
        else:
            connectionSocket.send(fileSize.encode('ascii'))
            upload(fileName)
    elif uploadfile.match(data):
        data = data.split(" ")
        print("MSG: Recived upload command")
        fileName = data[1]
        fileSize = int(data[2])
        connectionSocket.send("ok".encode('ascii'))
        download(fileName, fileSize)
    else:
        connectionSocket.send("err".encode('ascii'))
        print("err")
# Close the socket
connectionSocket.close()
