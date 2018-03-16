# FTP Server Client
FTP server and FTP client. The client shall connect to the server and support uploading and downloading of files to/from server. Before

# Functions
* upload ( `<filename>` )
    * Returns ok for success
    * Returns <error message> for failure (such as file doesn't exist)
* download ( `<filename>` )
    * Returns ok for success
    * Returns <error message> for failure
* ls
    * Returns string for success
    * Returns False for failure
    * List of files in the current directory
* main
    * user inputs
    * main communication
        
    
# Protocol Design

## Ports
    
* Client Port: 1111
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

