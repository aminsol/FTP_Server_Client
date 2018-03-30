#!/usr/bin/python3
# This is client.py file
import socket

# For file transfer
FTP= 3333
# For communicating to Client
clientPort = 1111

# For communicating to server
serverPort = 2222

    # get local machine name
host = socket.gethostname()
    
    # create a socket object
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connection to hostname on the port.
clientSocket.connect((host, serverPort))

filename = input("Enter Filename: ")
if filename != 'q':
    
        # Sending the message
    clientSocket.send(filename)
    data = s.recv(1024)
    if data[:6] == 'EXISTS':
        filesize = long(data[6:])
        message = input("File Exists, "+(filesize)+\
                                "Bytes, download? (Y/N): ")
        if message == 'Y':
            clientSocket.send('OK')
            f = open('new_'+filename, 'wb')
            data = clientSocket.recv(1024)
            totalRecv = len(data)
            f.write(data)
            while totalRecv < filesize:
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                print ("{0:.2f}",format((totalRecv/float(filesize))*100)+\
                    "% Done")
            print ("Downlad Complete!")
    else:
        print ("File does not exist")
                
clientSocket.close()
print   ("Client connection Closed!")
