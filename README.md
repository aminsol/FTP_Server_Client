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

## Client 

### Commands:
    ls
	upload <File Name>
	download <File Name>

### Responses:
    ok (message received with no error)
	err <message>
	
* Ports: 1111
* File Transfer Port: 3333

## Server
	
### Responses:
    ok (message received with no error)
	err <message>
	(ls) <list of directories>
* Ports: 2222
* File Transfer Port: 3333

