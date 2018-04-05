#!/usr/bin/python3
# This is client.py file
import socket, sys, os

# For data transfer to/from CLient/server
FTP = 2222
hostt = "127.0.0.1"
def getSize(file):
    fs = os.stat(file) # asume file is in same dir as the client file 
    return fs.st_size  # return size 

def uploadFile(clientCommSocket, host, uInput): # pass communication socket hostname and file name
    try:
        fObj = open(uInput, "rb")
        fileSize = str(getSize(uInput)).encode('utf-8')

        clientCommSocket.send(uInput.encode('utf-8'))
        ackMsg = clientCommSocket.recv(1024).decode("utf-8").strip()
        while ackMsg != "r":
            clientCommSocket.send(uInput.encode('utf-8'))
        
        clientCommSocket.send(fileSize)
        ackMsg = clientCommSocket.recv(1024).decode("utf-8").strip()
        while ackMsg != "r":
            clientCommSocket.send(fileSize)
        print ("Sent filename: " + uInput + " size " + str(getSize(uInput)) + "\n")

        clientCtrSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientCtrSocket.connect((host, FTP))
        print("FTP connection established commncing upload")
        bytesSent = 0
        while bytesSent < int(fileSize):
            fileData = fObj.read()
            if fileData:
                bytesSent += clientCtrSocket.send(fileData)
            print("Sent: " + str(bytesSent) + " / " + str(fileSize).decode() )
        print("File upload done...\n")
        fObj.close()
    except FileNotFoundError:
        print("File not found...")
    except ConnectionError:
        print("Error connecting to FTP port \n")

def main(): # this is for me the upload file function is the important part 
    try: #check that valid port number has been passed
        serverMachine = str(sys.argv[1])
        commPort  = int(sys.argv[2]) # attempt to assign port number to FTP
    except IndexError:
        print("Invalid server name / port number: usage 'python3 client.py <server machine> <port number>'\n")
        sys.exit()
    except ValueError: # if something other than int was sent we get value error
        print("Invalid server name / port number: usage 'python3 client.py <server machine> <port number>\n")
        sys.exit()

    # connection to hostname on the port. to test use loopback adress 127.0.0.1
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket object
        clientSocket.connect((serverMachine, commPort))  # connection to hostname on the port. to test use loopback adress 127.0.0.1
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
                uploadFile(clientSocket, serverMachine, uInput[1]) # should have file name in uInput[1]
            elif uInput[0] == "ls": # Karla
                pass
        except IndexError:
            print("No filename provided: get <filename> / put <filename>")


    clientSocket.close()
    print("Client connection Closed!")


main()