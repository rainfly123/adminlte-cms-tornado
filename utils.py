#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
import hashlib
import os
import statvfs
from mutagen import mp3


GB = 1024 * 1024 * 1024

def GetMd5(inputs):
    if inputs is not None:
        md5 = hashlib.md5()
        md5.update(inputs)
        return md5.hexdigest()

def GetUsage():
    df = os.statvfs("/")
    Total = (df.f_bsize * df.f_blocks) / GB
    Free = (df.f_bsize * df.f_bfree) / GB
    Avaiable = round(float(Free) / Total, 2)
    return Free, Total - Free, int((1 - Avaiable)*100)

def GetDuration(filepath):
    if filepath is not None:
        audio = mp3.Open(filepath)
        return int(audio.info.length)
        

if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print "Usage: %s [filename]"%(sys.argv[0])
        sys.exit(0)

    print "Caculating the md5 of %s..."%(sys.argv[1])
    with open(sys.argv[1]) as fs:
        data = fs.read()
        print GetMd5(data)

    print GetDuration(sys.argv[1])

    a,b,c = GetUsage()
    print a,b,c

    
