#!/usr/bin/python3
# This is server.py file
import socket
import threading
import os

# The ports on which to listen

# For file transfer
FTP = 3333

# For communicating to Client
clientPort = 1111

# function to uplad file
def RetrFile(name, sock):
    filename = sock.recv(1024)
    if os.path.isfile(filename):
        sock.send("EXISTS " + str(os.path.getsize(filename)))
        userResponse = sock.recv(1024)
        if userResponse[:2] == 'OK':
            with open(filename, 'rb') as f:
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
                    while bytesToSend != "":
                        bytesToSend = f.read(1024)
                        sock.send(bytesToSend)
    else:
            sock.send("ERR")

    sock.close()

def Main():
    # For communicating to server
    serverPort = 2222
    
    # get local machine name
    host = socket.gethostname()
    
    # Create a TCP socket
    serverSocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    serverSocket.bind((host,serverPort))

    # Start listening for incoming connections
    serverSocket.listen(serverPort)

    print("The server is ready to receive")

    # The buffer to storetherreceived data
    data=""

    # Forever accept incoming connections
    while True:
        # Accept a connection; get client’s socket
        connectionSocket,addr=serverSocket.accept()
        print ("client connected ip: <" + str(addr)+ ">")
        thread = threading.Thread(target = RetrFile, args=("retrThread", connectionSocket))
        thread.start()
       
    
    # Close the socket
    serverSocket.close()

if __name__ == "__main__":
    Main()
