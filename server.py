#!/usr/bin/python3
#This is server.py file
import socket

#Theportonwhichtolisten
serverPort = 12000

#CreateaTCPsocket
serverSocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bindthesockettotheport
serverSocket.bind(('',serverPort))

#Startlisteningforincomingconnections
serverSocket.listen(12000)

print("The server is ready to receive")

#Thebuffertostoretherreceiveddata
data=""

#Foreveracceptincomingconnections
while True:
    #Acceptaconnection;getclient’ssocket
    connectionSocket,addr=serverSocket.accept()
    #Receivewhateverthenewlyconnectedclienthastosend
    data = connectionSocket.recv(40)
    print(data)

    #Closethesocket
    connectionSocket.close()