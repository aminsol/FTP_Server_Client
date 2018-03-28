#!/usr/bin/python3
# This is client.py file
import socket
from ftplib import FTP

# For file transfer
FTP= 3333




filename = "text.html"
# For communicating to server
serverPort = 2222
# For communicating to Client
clientPort = 1111

# create a socket object
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ftp = FTP(severrDomain)
ftp.login(user="",passwd="")

# get local machine name
host = socket.gethostname()

# connection to hostname on the port.
clientSocket.connect((host, serverPort))

# Our message
data = b"Hello World! This is a very long string."

# Sending the message
clientSocket.send(data)

clientSocket.close()
ftp.quit()
print("Client connection Closed!")
