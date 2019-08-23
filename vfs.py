#!/usr/bin/env python
import os
import statvfs

GB = 1024 * 1024 * 1024
def GetUsage():
    df = os.statvfs("/")
    Total = (df.f_bsize * df.f_blocks) / GB
    Free = (df.f_bsize * df.f_bfree) / GB
    Avaiable = round(float(Free) / Total, 2)
    return Free, Total - Free, int((1 - Avaiable)*100)

if __name__ == "__main__":
    a,b,c = GetUsage()
    print a,b,c
