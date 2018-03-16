#!/usr/bin/python3
# This is client.py file
import socket

# create a socket object
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 3413

# connection to hostname on the port.
clientSocket.connect((host, port))

# Our message
data = b"Hello world"

# Sending the message
clientSocket.send(data)

clientSocket.close()
print("Client connection Closed!")