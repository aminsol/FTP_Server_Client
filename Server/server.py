#!/usr/bin/python3
# This is server.py file
#fernando's part
import socket
import sys, os, time

# For data transfer to/from CLient/server
FTP = 2222

def retrieveUpload (connSocket, requester): # pass it the connection socket and person requesting
    filename = connSocket.recv(1024).decode("utf-8").strip() # get name and remove any garbage 
    connSocket.send(b"r")
    fileSize = connSocket.recv(1024).decode("utf-8").strip()
    connSocket.send(b"r")
    print ("Recieved upload request for file: " + filename + " with size: " + fileSize + " bytes\n")
    print ("Commencing upload request from client:" + requester + " for " + filename + "\n")

    serverCtrSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverCtrSocket.bind(('', FTP))
    serverCtrSocket.listen(20)
    print("Established FTP port waiting for client connection...")
    ctrlSock, add = serverCtrSocket.accept()

    print("FTP connection established commencing client file upload...\n")
    bytesRcv = 0
    filedata = ""
    fObj = open(filename, "w")
    while bytesRcv < int(fileSize):
        filedata += ctrlSock.recv(1024).decode()
        bytesRcv += len(filedata)
        print("Rcv'ed: " + str(bytesRcv) + " / " + fileSize )
    
    fObj.write(filedata)
    print ("File recived and stored")
    ctrlSock.close()


# Forever accept incoming connections
def s_main(): # again just for me, retrieveUpload is the important file
    try: #check that valid port number has been passed
        commPort  = int(sys.argv[1]) # attempt to assign port number to FTP
    except IndexError: # if no argument was sent then we get index error
        print("Invalid port number: usage 'python3 server.py <port number>'\n")
        sys.exit()
    except ValueError: # if something other than int was sent we get value error
        print("Invalid port number: usage 'python3 server.py <port number>'\n")
        sys.exit()


    # Create a TCP socket
    serverSocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    serverSocket.bind(('',commPort))

    # Start listening for incoming connections
    serverSocket.listen(20) # 20 conncurent listens 
    # not in loop for easier testing 
    print("The server is ready to receive communication on port " + str(commPort) + "\n")

    # Accept a connection; get client’s socket
    connectionSocket,addr=serverSocket.accept()
    # Receive whatever the newly connected client has to send
    print("Connection from client: " + str(addr) + "\n")

    retrieveUpload(connectionSocket, str(addr)) # attempt to get upload
    
    # Close the socket
    connectionSocket.close()


s_main()