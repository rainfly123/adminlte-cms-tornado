#!/usr/bin/env python
import os
def download(url):
    os.system("wget {0}".format(url))

f = open("files")
lines = f.readlines()
for line in lines:
   line = line.strip()
   size,url = line.split()
   filen = os.path.basename(url)
   if os.path.exists(filen):
       filesize = os.stat(filen).st_size
       print filesize, size, filen
       if filesize != int(size):
           os.remove(filen)
           download(url)
   else:
       download(url)
