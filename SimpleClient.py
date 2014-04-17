#!/usr/bin/python

import socket
import sys
import os
import random
import getopt


s = socket.socket()
host = ''
port = ''
filename = ''

usage = 'SimpleClient.py -f <filename> -s <hostname> -p <portname>'
try:
	opts, args = getopt.getopt(sys.argv[1:], "hf:s:p:")
except getopt.GetoptError:
	print usage
	sys.exit()
for opt, arg in opts:
	if opt == '-h':
		print usage
		sys.exit()
	elif opt == '-f':
		filename = arg 
	elif opt == '-s':
		host = arg
	elif opt == '-p':
		port = int(arg)
if filename == '' or host == '' or port == '':
	print usage
	sys.exit()

try:
	s.connect((host,port))
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
