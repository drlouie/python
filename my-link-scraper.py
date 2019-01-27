#!/usr/bin/env python

#- Extensible library for opening URLs
import urllib2
#- Regular expression operations
import re

#- Request user input, with an example of what is expected as input
userInputURL    = raw_input("Enter URL to search, for example, http://w3c.org/:")
#- Use urllib2 to open a connection the URL input by the user
dataConnection = urllib2.urlopen(userInputURL)
#- Read the query response
websiteData = dataConnection.read()
#- User a regular expression to extract all chunks of text with http://, https://, ftp:// or ftps://, in turn having scraped all links from within the document
allLinks = re.findall('"((http|ftp)s?://.*?)"', websiteData)
#- Print our results, by default, as JSON
print allLinks
