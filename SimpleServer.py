#!/usr/bin/python

import socket

class UserError(Exception):
	def __init__(self, message):
		self.message = message
	def __str__(self):
		return repr(self.message)
		
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
		try:
			if len(filename) == 0:
				raise UserError('No filename recived')

			if len(ext.intersection(whitelist)) != 1:
				raise UserError('Sorry! This format is not in whitelist')

			with open(filename, "r") as myfile:
				data = myfile.read()
				c.send('\x00'+data)

		except UserError as e:	
			c.send('\x01' + e.message)	
		except Exception, e:
			c.send('\x02' + str(e))
			
		c.close()
