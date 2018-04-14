# FTP Server Client

### Team

    Amin Soltani
    Elias Perez
    Fernando Cuevas
    Karla Lugo


FTP server and FTP client. The client shall connect to the server and support uploading and downloading of files to/from server.

### Language

    Python 3.6

### Functions

    upload ( <filename> ) client and server
        Returns ok for success
        Returns <error message> for failure (such as file doesn't exist)

    download ( <filename> ) client and server
        Returns ok for success
        Returns <error message> for failure

    ls server only
        Returns string for success
        Returns False for failure
        List of files in the current directory

    main
        user inputs
        main communication

## Protocol Design Ports

    Server Port: 2222
    File Transfer Port: 3333

### Client Commands:

 `ls`

 `upload <File Name>`

 `download <File Name>`


File Transfer Port: 3333

### Server Responses:

 `(ls) <list of directories>`

 `ok (message received with no error)`

 `err <message>`

    Ports: 2222
    File Transfer Port: 3333

Example code:

    From client side
        peg_asus@DESKTOP-VUOEPEK:~/Documents/FTP_Server_Client/Client$ python3 client.py DESKTOP-VUOEPEK 1234
        Enter your command: ls
            a.txt
            server.py
            Enter your command: download b.txt
            No such file found on the server!
        Enter your command: download a.txt
        Start downloading..
        file size: 3552
        Total Recieved: 1024
        Total Recieved: 2048 / 3552
        Total Recieved: 3072 / 3552
        Total Recieved: 3552 / 3552
        None
        Download is finished!
        Enter your command: upload c.txt
        No such file found locally...
        Enter your command: upload foo_new.png
        FTP connection established commncing upload
        Sent: 271296 / 271296
        File upload done...

        Enter your command: ls
        a.txt
        foo_new.png
        server.py
        Enter your command: exit
        Client connection Closed!

 Server side:

     Server Port: 1234
     The server is ready to receive
     Established Connection with: ('127.0.0.1', 57207)
     MSG: Recived ls command
     Established Connection with: ('127.0.0.1', 57208)
     MSG: Recived download command
     File requested not found sending err msg...
     Established Connection with: ('127.0.0.1', 57210)
     MSG: Recived download command
     FTP connection established commncing upload
     File a.txt upload done...



    Established Connection with: ('127.0.0.1', 57212)
    MSG: Recived upload command
    file size: 271296
    Total Recieved: 1024
    Total Recieved: 2048
    Total Recieved: 3072
    Total Recieved: 4096
    Total Recieved: 5120
    Total Recieved: 6144
    Total Recieved: 40960
    Total Recieved: 41984
    Total Recieved: 48128
    Total Recieved: 49152
    ...
    ... Omitted to save space
    ...
    Total Recieved: 247808
    Total Recieved: 248832
    Total Recieved: 249856
    Total Recieved: 271296
    Upload from client complete...