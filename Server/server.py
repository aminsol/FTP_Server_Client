#!/usr/bin/python3
# This is server.py file
#fernando's part
import socket
import sys, os


def recvData(sock, nBytes):
    rBuffer = ""
    tmpBuffer = ""
    while len(rBuffer) < nBytes:
        tmpBuffer = sock.recv(nBytes)

        if not tmpBuffer:
            break
        rBuffer += str(tmpBuffer)
    
    return rBuffer


# Forever accept incoming connections
def s_main():
    try: #check that valid port number has been passed
        listenPort  = int(sys.argv[1]) # attempt to assign port number to FTP
    except IndexError: # if no argument was sent then we get index error
        print("Invalid port number: usage 'python3 server.py <port number>'\n")
        sys.exit()
    except ValueError: # if something other than int was sent we get value error
        print("Invalid port number: usage 'python3 server.py <port number>'\n")
        sys.exit()
    
    # For data transfer to/from CLient/server
    FTP = 2222
    # For communicating to/from Client/Server
    commPort = 1111

    # Create a TCP socket
    serverSocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    serverSocket.bind(('',listenPort))

    # Start listening for incoming connections
    serverSocket.listen(commPort)

    print("The server is ready to receive")

    # The buffer to storetherreceived data
    data=""

    while True:
        # Accept a connection; get client’s socket
        connectionSocket,addr=serverSocket.accept()
        # Receive whatever the newly connected client has to send
        print("Connection from client: " + str(addr) + "\n")

        fileData = ""
        rBuffer = ""
        fSize = 0
        fsBuffer = ""

        fsBuffer = recvData(connectionSocket, 10)
        fSize = len(fsBuffer)

        fileData = recvData(connectionSocket, fSize)

        print(fileData)

        # Close the socket
        connectionSocket.close()


s_main()