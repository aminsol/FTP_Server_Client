# FTP_Server_Client
FTP server and FTP client. The client shall connect to the server and support uploading and downloading of files to/from server. Before

## Client 

#### Commands:
	upload
	download
	ls
	ok (message received with no error)
	err
#####Port: 1111

## Server commands:
	reject(file does not exist)
	send <port#>
	receive <port#>
	<list of directories>
	ok (message received with no error)
	err
##### Port: 2222

