#!/usr/bin/python3
# This is client.py file
import socket

# For file transfer
FTP = 3333
# For communicating to server
serverPort = 2222
# For communicating to Client
clientPort = 1111

# create a socket object
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# connection to hostname on the port.
clientSocket.connect((host, serverPort))
command = input("Enter your commnad: ")


# Sending the message
clientSocket.send(command.encode('ascii'))

clientSocket.close()
print("Client connection Closed!")