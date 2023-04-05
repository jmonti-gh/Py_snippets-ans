### tinyurl.py

'''
How to Make URLs Shorter: large URLs can be quite annoying to read and share. To shorten the URLs, 
this script makes use of a third-party API.
'''

from __future__ import with_statement
import contextlib
try:
	from urllib.parse import urlencode
except ImportError:
	from urllib import urlencode
try:
	from urllib.request import urlopen
except ImportError:
	from urllib3 import urlopen
import sys

def make_tiny(url):
	request_url = ('http://tinyurl.com/app-index.php?' + 
	urlencode({'url':url}))
	with contextlib.closing(urlopen(request_url)) as response:
		return response.read().decode('utf-8')

def main():
	for tinyurl in map(make_tiny, sys.argv[1:]):
		print(tinyurl)

if __name__ == '__main__':
	main()