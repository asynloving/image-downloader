#!/usr/bin/env python
#coding: utf-8

import os
import sys
import urllib
from BeautifulSoup import BeautifulSoup

try:
	url = sys.argv[1]
	directory = sys.argv[2]
except:
	print "$ downloader.py [url] [directory]"
	sys.exit(1)


# get image urls from url

soup = BeautifulSoup(urllib.urlopen(url).read())
image_urls = []
for tag in soup.findAll("a"):
	if tag.img:
		ext = os.path.splitext(tag.img["src"])[1]
		allow_exts = [".jpg",".JPG",".png",".PNG"]
		if ext in allow_exts:
			image_urls += [tag.img["src"]]

# move directory
if os.path.isdir(directory):
	os.chdir(directory)

else:
	os.mkdir(directory)
	os.chdir(directory)

# download images to directory
for url in image_urls:
	if url.startswith("https://"):
		cmd = "wget --quiet --no-check-certificate %s" % url
	else:
		cmd = "wget --quiet %s" % url

	# log
	print "Downloading... %s" % url.split("/")[-1]
	os.system(cmd)

print "Complete!"
