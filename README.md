# FTP Server Client
FTP server and FTP client. The client shall connect to the server and support uploading and downloading of files to/from server. Before

# Client 

### Commands:
    ls
	upload <File Name>
	download <File Name>
	cancel (cencelling file transfer)

### Responses:
    ok (message received with no error)
	err <message>
	
* Ports: 1111
* File Transfer Port: 3333

# Server

### Commands:
	upload <File Name>
	download <File Name>
	cancel (cencelling file transfer)
	
### Responses:
    ok (message received with no error)
	err <message>
	(ls) <list of directories>
* Ports: 2222
* File Transfer Port: 3333

