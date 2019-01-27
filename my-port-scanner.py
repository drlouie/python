#!/usr/bin/env python

#- Low-level networking interface
import socket
#- Allows you to spawn new processes
import subprocess
#- System-specific parameters and functions
import sys
#- Basic date and time types
from datetime import datetime

#- clear the screen
subprocess.call('clear', shell=True)
#- Request user's IP address or host name input
remoteMachine    = raw_input("Enter a host to start scanning:")
#- Use socket to gethostbyname, IP address, of whatever the user has input into the terminal
remoteMachineIP  = socket.gethostbyname(remoteMachine)

#- in a new line, print out 55 dashes to the screen
print "-" * 55
#- in a new line, print out the following to the screen
print "Scanning", remoteMachineIP, " please wait..."
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
	#- Check for open IP:port combo
        result = connection.connect_ex((remoteMachineIP, port))
	#- If result is 0
        if result == 0:
		#- Print result to terminal
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

#- Find how long it took to finish this request
timeDifference =  endProcess - startProcess

#- Let user know how long it took to finish their request
print 'Scanning completed in ', timeDifference
