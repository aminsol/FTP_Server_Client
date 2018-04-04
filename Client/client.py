"""  
    client.py
    
    CPSC 471 Group
    
    This client program does the following:
        1. Create a TCP connection to the server
        2. Ask the client to input the name of a file
        3. Receive the response from server. If the response is 'yes', then start using TCP
           transfer to receive the file. If the response is 'no', then give the client a
           prompt and exit.
"""

from socket import *
import os

# server machine's name
host = "127.0.0.1"

# port numbers of server
server = 2222
ftp= 3333

def getSize(filename):
    st = os.stat('/Users/eliasperez/Documents/GitHub/FTP_Server_Client/Server/'+filename)
    return st.st_size

# start using TCP transfer to transfer the file
def RetrFile():
        # create TCP transfer socket on client to use for connecting to remote
        # server. Indicate the server's remote listening port
        clientSocket_transf = socket(AF_INET,SOCK_STREAM)
        
        # open the TCP transfer connection
        clientSocket_transf.connect((host,ftp))
        
        # connection prompt
        print("TCP transfer connected. | Server: %s, Port: %d" % (host, ftp))
        

        # get the data back from the server
        filedata = clientSocket_transf.recv(1024)
        
        # creat a file named "filename" and ready to write binary data to the file
        filehandler = open(filename, 'wb')
        filesize = getSize(filename)
        totalRecv = len(filedata)        # write the data to the file
        filehandler.write(filedata)
        print("file size: %d " % filesize)
        print("Total Recieved: %d " % totalRecv)
        while totalRecv < filesize:
            filedata = clientSocket_transf.recv(1024)
            totalRecv = totalRecv + len(filedata)
            filehandler.write(filedata)
            print("Total Recieved: %d " % totalRecv)
        print("Do i get here?")
    
        
        # close the file
        filehandler.close()
        
        # close the TCP transfer connection
        return clientSocket_transf.close()


# create TCP socket on client to use for connecting to remote
# server. Indicate the server's remote listening port
clientSocket_ctrl = socket(AF_INET, SOCK_STREAM)

# open the TCP control connection
clientSocket_ctrl.connect((host,server))

# connection prompt
print("TCP control connected. | Server: %s, Port: %d" % (host, server))

# input the file name client wants
filename = input("Input file name: ")

# send the file name to the server
clientSocket_ctrl.send(bytes(filename, "utf-8"))

# get the status of the file from server "yes" or "No"
filestatus = clientSocket_ctrl.recv(1024).decode("utf-8").strip()

# check whether the file is on the server. If yes, receive the file.
# If no, do give a prompt
if filestatus == "yes":
        # download prompt
        print("Start downloading..")
        
        # start using TCP transfer
        RetrFile()
        
        # success prompt
        print("Done!")
else:
    # cannot find the file on the server
    print("No such file found on the server!")

# close the TCP control connection
clientSocket_ctrl.close()
