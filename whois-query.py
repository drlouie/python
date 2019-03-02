#!/usr/bin/env python

#- System-specific parameters and functions
import sys
#- WHOIS query module for Python
import whois
#- Low-level networking interface
import socket

#- Basic date and time types
from datetime import datetime

# define the whoisQuery method
def whoisQuery(DomainNameToQuery):
	#- in a new line, print out 55 dashes to the screen
	print "-" * 55
	#- in a new line, print out the following to the screen
	print "Querying WHOIS for", DomainNameToQuery, "please wait..."
	#- in a new line, print out 55 dashes to the screen
	print "-" * 55

	#- Take note of the time we start processing this user request
	startProcess = datetime.now()

	#- Try
	try:
	
		#- Run WHOIS query on DomainNameToQuery using the Python WHOIS module
		results = whois.whois(DomainNameToQuery)

		#- Print the raw results to the client
		print results
		
	#- Catch exception
	except:
			print "There was an error with your request"
		#- Exit gracefully
			sys.exit()

	#- Take note of the time we end processing this user request
	endProcess = datetime.now()

	#- Find how long it took to process this request, by subtracting the startProcess time from the endProcess time
	timeDifference =  endProcess - startProcess

	#- in a new line, print out 55 dashes to the screen
	print "-" * 55
	#- Let user know how long it took to process their request
	print 'Querying completed in', timeDifference
	#- in a new line, print out 55 dashes to the screen
	print "-" * 55

#- Request domain name input since no command line argument has been introduced
if len(sys.argv) is 1:
	domainName = raw_input("Enter a domain name to initiate a WHOIS query:")
#- Use command line argument as domain to query
else:
	domainName = sys.argv[1]

#- Use socket to gethostbyname, IP address, of whatever the user has input into the terminal
DomainIpVerify  = socket.gethostbyname(domainName)
#- If domainName is set
if DomainIpVerify is not None:
	#- Run a whoisQuery on domainName
	whoisQuery(domainName)