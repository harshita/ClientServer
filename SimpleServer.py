#!/usr/bin/python

import socket


if __name__ == "__main__":
	s = socket.socket()
	#host = socket.gethostname()
	host = '0.0.0.0'
	port = 12345
	s.bind((host,port))

	s.listen(5)
	whitelist = set(['.txt','.xml','.json'])
	while True:
		c,addr = s.accept()
		filename=c.recv(1024)
		print 'Got connection from', addr
		extindex=filename.index(".")
		ext=set([filename[extindex:]])
		if filename!="":
			if len(ext.intersection(whitelist))==1:
				try:
					with open(filename, "r") as myfile:
						data=myfile.read()
						c.send('\x00'+data)
				except:
					c.send('\x01Unable to open a file')
			else:
				c.send('\x01Sorry!This format is not in whitelist')
		else:
			c.send('\x01No file name received')
		c.close()
