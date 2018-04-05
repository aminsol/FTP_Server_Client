#!/usr/bin/python3
# This is server.py file
import socket

# The ports on which to listen

# For file transfer
FTP = 3333
# For communicating to server
serverPort = 2222
# For communicating to Client
clientPort = 1111

# Create a TCP socket
serverSocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
serverSocket.bind(('',serverPort))

# Start listening for incoming connections
serverSocket.listen(serverPort)

print("The server is ready to receive")

# The buffer to storetherreceived data
data=""

# Forever accept incoming connections
while True:
    # Accept a connection; get client’s socket
    connectionSocket,addr=serverSocket.accept()
    # Receive whatever the newly connected client has to send
    data = connectionSocket.recv(40)
    print(data)
    
    
#this should list the dirctories    
    import os
def files(path):  
    for file in os.listdir(path):
        #os.path.isfile() returns True if the given entry is a file.
        if os.path.isfile(os.path.join(path, file)):
            yield file

for file in files("."):  
    print (file)

    # Close the socket
    connectionSocket.close()
