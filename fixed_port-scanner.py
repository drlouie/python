#!/usr/bin/env python

#- Low-level networking interface
import socket
#- Allows you to spawn new processes
import subprocess
#- System-specific parameters and functions
import sys

#- Basic date and time types
from datetime import datetime

# define the portScan method
def portScan(IpToScan):
	#- in a new line, print out 55 dashes to the screen
	print "-" * 55
	#- in a new line, print out the following to the screen
	print "Scanning", IpToScan, " please wait..."
	#- in a new line, print out 55 dashes to the screen
	print "-" * 55

	#- Take note of the time we start processing this user request
	startProcess = datetime.now()

	#- Try
	try:
		#- Look for open ports between 1 and 100
		for port in range(1,100):  
			#- Initiate the socket for a connection
			connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			#- Set a timeout for each connection attempt, set too low or too high will cause issues
			connection.settimeout(0.05)
			#- Check for open IP:port combo
			result = connection.connect_ex((IpToScan, port))
			#- If result is 0, meaning there was a result
			if result == 0:
				#- Print to terminal
				print "Port {}'s open" . format(port)
			#- Close socket connection
			connection.close()

	#- Exception: Process interrupted
	except KeyboardInterrupt:
			print "You hit Ctrl + C"
		#- Exit gracefully
			sys.exit()

	#- Exception: GetAddrInfo error
	except socket.gaierror:
		print 'Could not resolve the hostname.'
		#- Exit gracefully
		sys.exit()

	#- Exception: Unable to connect
	except socket.error:
		print "No server connection available."
		#- Exit gracefully
		sys.exit()

	#- Take note of the time we end processing this user request
	endProcess = datetime.now()

	#- Find how long it took to finish this request, by subtracting the startProcess time from the endProcess time
	timeDifference =  endProcess - startProcess

	#- Let user know how long it took to finish their request
	print 'Scanning completed in ', timeDifference

#- Request user's IP address or host name input since no command line argument has been introduced
if len(sys.argv) is 1:
	remoteMachine = raw_input("Enter a host to start scanning:")
#- Use command line argument as host to scan
else:
	remoteMachine = sys.argv[1]

#- Try:
try:
	#- Using socket to gethostbyname, IP address, of whatever the user has input into the terminal
	IpToScan  = socket.gethostbyname(remoteMachine)
#- Catch any problems, we call then call it an unresolvable host
except:
	#- Set IpToScan variable to None for later use
	IpToScan = None
	#- Let user know the fate of their request
	print "Could not resolve host"

#- If IpToScan is set then we run a portScan on it
if IpToScan is not None:
	#- Run a portscan on IpToScan
	portScan(IpToScan)
