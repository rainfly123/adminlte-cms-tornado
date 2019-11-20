#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
import hashlib
import os
from mutagen import mp3

def GetSize(filepath):
    if filepath is not None:
        s = os.stat(filepath)
        return s.st_size

def GetMd5(filepath):
    if filepath is not None:
        md5 = hashlib.md5()
        with open(filepath) as fs:
            data = fs.read()
            md5.update(data)
            return md5.hexdigest()

def GetDuration(filepath):
    if filepath is not None:
        audio = mp3.Open(filepath)
        return int(audio.info.length)

def GetBitrate(filepath):
    if filepath is not None:
        audio = mp3.Open(filepath)
        return int(audio.info.bitrate)
        
def GetSampleRate(filepath):
    if filepath is not None:
        audio = mp3.Open(filepath)
        return int(audio.info.sample_rate)
 

if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print "Usage: %s [filename]"%(sys.argv[0])
        sys.exit(0)

    print GetDuration(sys.argv[1])
    print GetMd5(sys.argv[1])
    print GetSize(sys.argv[1])
    print GetBitrate(sys.argv[1])/1000,"k"
    print GetSampleRate(sys.argv[1])/1000,"k"


    
