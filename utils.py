#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
import hashlib
import os
import statvfs
#import librosa


GB = 1024 * 1024 * 1024

def GetMd5(inputs):
    if inputs is not None:
        md5 = hashlib.md5()
        md5.update(inputs)
        return md5.hexdigest()

def GetMp3Duration(filepath):
    if filepath is not None:
        pass


def GetUsage():
    df = os.statvfs("/")
    Total = (df.f_bsize * df.f_blocks) / GB
    Free = (df.f_bsize * df.f_bfree) / GB
    Avaiable = round(float(Free) / Total, 2)
    return Free, Total - Free, int((1 - Avaiable)*100)


if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print "Usage: %s [filename]"%(sys.argv[0])
        sys.exit(0)

    print "Caculating the md5 of %s..."%(sys.argv[1])
    with open(sys.argv[1]) as fs:
        data = fs.read()
        print GetMd5(data)

    print GetMd5(None)

    a,b,c = GetUsage()
    print a,b,c
