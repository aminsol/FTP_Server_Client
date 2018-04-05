#!/usr/bin/python3
# This is client.py file
import socket, sys, os

def getSize(file):
    fs = os.stat(file)
    return fs.st_size

def uploadFile(clientSocket, commPort, uInput):
    try:
        fObj = open(uInput, "r")
        fileSize = getSize(uInput)
        bytesSent = 0 # keep track of bytes sent
        ack = 0  # acknolage that the bytes were recievced
        #clientSocket.send(b"u") # send upload command to server
        fileData = None
        while True:
            fileData = fObj.read(65536)
            if fileData:
                dataSizeStr = str(len(fileData))
                while len(dataSizeStr) < 10:
                    dataSizeStr = "0" + dataSizeStr

                fileData += dataSizeStr
                while len(fileData) > bytesSent:
                    bytesSent += clientSocket.send(bytearray(fileData[bytesSent:], 'utf-8'))
            else:
                break
        fObj.close()
    except FileNotFoundError:
        print("File not found...")

def main():
    try: #check that valid port number has been passed
        serverMachine = str(sys.argv[1])
        serverPort  = int(sys.argv[2]) # attempt to assign port number to FTP
    except IndexError:
        print("Invalid server name / port number: usage 'python3 client.py <server machine> <port number>'\n")
        sys.exit()
    except ValueError: # if something other than int was sent we get value error
        print("Invalid server name / port number: usage 'python3 client.py <server machine> <port number>\n")
        sys.exit()

    # For data transfer to/from CLient/server
    FTP = 2222
    # For communicating to/from Client/Server
    commPort = 1111

    # create a socket object
    # get local machine name
    # host = socket.gethostname()

    # connection to hostname on the port. to test use loopback adress 127.0.0.1
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket object
        clientSocket.connect((serverMachine, serverPort))  # connection to hostname on the port. to test use loopback adress 127.0.0.1
    except ConnectionError:
        print("Error connecting to " + str(serverMachine) + "\n")
    except socket.gaierror:
        print("Unknown name or service")

    uInput = [""] # user input and while loop 
    print("Connection to server successful")
    while (uInput[0] != "quit"):
        uInput = input("ftp> ").split(" ")
        try:
            if uInput[0] == "get": # Elias
                pass
            elif uInput[0] == "put": # fernando
                uploadFile(clientSocket, commPort, uInput[1]) # should have file name in uInput[1]
            elif uInput[0] == "ls": # Karla
                pass
        except IndexError:
            print("No filename provided: get <filename> / put <filename>")


    clientSocket.close()
    print("Client connection Closed!")


main()