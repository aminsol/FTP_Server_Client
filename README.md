# FTP Server Client
FTP server and FTP client. The client shall connect to the server and support uploading and downloading of files to/from server.
# Language
 * Python 3.6
# Functions
* __upload ( `<filename>` )__ _client and server_
    * Returns `ok` for success
    * Returns `<error message>` for failure (such as file doesn't exist)
    
* __download ( `<filename>` )__ _client and server_
    * Returns `ok` for success
    * Returns `<error message>` for failure
    
* __ls__ _server only_
    * Returns string for success
    * Returns False for failure
    * List of files in the current directory
    
* __main__
    * user inputs
    * main communication
        
    
# Protocol Design

## Ports

* Server Port: 2222
* File Transfer Port: 3333

## Client 

### Commands:
    ls
	upload <File Name>
	download <File Name>
	
* Ports: 1111
* File Transfer Port: 3333

## Server

### Responses:

	(ls) <list of directories>
    ok (message received with no error)
	err <message>
* Ports: 2222
* File Transfer Port: 3333

# Team
 * Amin Soltani
 * Elias Perez
 * Fernando
 * Karla

