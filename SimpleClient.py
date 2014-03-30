#!/usr/bin/python

import sys
import remote

if __name__ == "__main__":

	if len(sys.argv)<2:
		print 'Please provide the name of the file to read'
	else:
		try:
			remote.copy('arjuna',12345,sys.argv[1])	
		except Exception, e:
			print e 
