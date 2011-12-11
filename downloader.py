#!/usr/bin/env python
#coding: utf-8

import os
import sys
import urllib
import datetime
from BeautifulSoup import BeautifulSoup

print "Image Downloader ver 1.0.3"

try:
	url = sys.argv[1]
	directory = sys.argv[2]
except:
	print "$ downloader.py [url] [directory]"
	sys.exit(1)

print "Donwload URL : %s" % url

# logging
print "logging..."
now_datetime = datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S")
log_file = os.environ["HOME"]+"/image-downloader.log"
dir = os.getcwd() if directory == "." else os.path.normpath(os.path.join(os.getcwd(),directory))
if os.access(log_file, os.F_OK):
	fp = open(log_file,"a+")
else:
	fp = open(log_file,"w")

logger = "Date : %s - %s to [%s]\n" % (now_datetime, url, dir)
fp.write(logger)
fp.close()
	


# get image urls from url

soup = BeautifulSoup(urllib.urlopen(url).read())
image_urls = []
for tag in soup.findAll("a"):
	if tag.img:
		url = tag["href"]
		ext = os.path.splitext(url)[1]
		allow_exts = [".jpg",".JPG",".png",".PNG"]
		if ext in allow_exts:
			image_urls += [url]

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
