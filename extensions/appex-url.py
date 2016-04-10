# coding: utf-8

import appex
import requests

from urlparse import urlparse
from urllib import url2pathname

def main():
	if not appex.is_running_extension():
		print 'Running in Pythonista app, using test data...\n'
		url = 'http://example.com/home'
	else:
		url = appex.get_url()
	if url:
		# TODO: Your own logic here...
		print 'Input URL: %s' % (url,)
		p = urlparse(url)
		print(p.path)
	else:
		print 'No input URL found.'

if __name__ == '__main__':
	main()