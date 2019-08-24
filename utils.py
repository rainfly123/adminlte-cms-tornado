#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
import hashlib
#import librosa


def GetMd5(inputs):
    if inputs is not None:
        md5 = hashlib.md5()
        md5.update(inputs)
        return md5.hexdigest()

def GetMp3Duration(filepath):
    if filepath is not None:
        pass

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
