#!/usr/bin/env python
import urllib2
import re
userInputURL    = raw_input("Enter URL to search, for example, http://w3c.org/:")
dataConnection = urllib2.urlopen(userInputURL)
websiteData = dataConnection.read()
allLinks = re.findall('"((http|ftp)s?://.*?)"', websiteData)
print allLinks