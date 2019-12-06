#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
import os
import utils
import hashlib

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        if name.endswith("mp3") == False:
            continue
        fullpath = os.path.join(root, name)
        if utils.GetSampleRate(fullpath) != 22050:
            print fullpath
            m = hashlib.md5()
            data = open(fullpath, 'rb').read()
            m.update(data)
            md5 = m.hexdigest()
            cmd = "ffmpeg -i {0} -id3v2_version 3 -metadata artist='Qichen' -map_metadata -1 -ar 22050 -ab 64k ./md5/{1}.mp3".format(fullpath, md5))
            os.system(cmd)
        else:
            os.rename(fullpath, "../md5/{0}".format(fullpath))
    

