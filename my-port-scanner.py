#!/usr/bin/env python

import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)
remoteMachine    = raw_input("Enter a host to start scanning:")
remoteMachineIP  = socket.gethostbyname(remoteMachine)

print "-" * 55
print "Scanning", remoteMachineIP, " please wait..."
print "-" * 55

startProcess = datetime.now()

try:
    for port in range(1,100):  
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = connection.connect_ex((remoteMachineIP, port))
        if result == 0:
            print "Port {}'s open" . format(port)
        connection.close()

except KeyboardInterrupt:
    print "You hit Ctrl + C"
    sys.exit()

except socket.gaierror:
    print 'Could not resolve the hostname.'
    sys.exit()

except socket.error:
    print "No server connection available."
    sys.exit()

endProcess = datetime.now()

timeDifference =  endProcess - startProcess

print 'Scanning Completed in: ', timeDifference