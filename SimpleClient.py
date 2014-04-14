#!/usr/bin/python

import socket
import sys
import os
import random

s = socket.socket()
host = socket.gethostname()
port = 12345
if len(sys.argv)<2:
	print 'Please provide the name of the file to read'
else:
	try:
		s.connect((host,port))
		filename=sys.argv[1]
		print filename
		s.send(filename)
		fullmessage=""
	
		returncode=s.recv(1)
		while True:
			data=s.recv(5)
			if not data: break
			fullmessage=fullmessage+data
		s.close
		if ord(returncode)==0:
			tempname=filename
			extindex=filename.index(".")
			if extindex!=0:
				ext=filename[extindex:]
			while os.path.isfile(tempname):
				randnum=random.randint(1,10)
				file=tempname[:extindex]
				tempname=file+str(randnum)+ext
			print 'writing to new file '+tempname
			f = open(tempname,"w")
			f.write(fullmessage)
			f.close()
		else:
			print fullmessage	
	except:
		print 'Failed to connect to host:',host,' port:',port
