#!/usr/bin/env python
#coding:utf-8
import sys;
reload(sys);
sys.setdefaultencoding("utf8")
from qiniu import Auth
from qiniu import put_file, etag
import qiniu.config
import os
import hashlib

URL = "https://cdncms.qctchina.top"
access_key = 'pkTzM_Eu4vrIYJDuh4u5psLAWzycH7nozlWU2-Uz'
secret_key = 'P6JLYU87Oxc8cDjL5SWL6Ajfg1Nonm6NH09c60TN'

q = Auth(access_key, secret_key)
bucket_name = 'resource'

def upload(localfile):
    if os.path.exists(localfile) == False:
        return

    suffix = os.path.splitext(localfile)[1]
    keyname = localfile.strip()

    token = q.upload_token(bucket_name, keyname, 3600*100)
    ret, info = put_file(token, keyname, localfile)
    if ret['hash'] == etag(localfile):
        return os.path.join(URL, keyname)
    return None

if __name__ =='__main__':
    localfile = 'a.mp3'
    lines = open("nmd5s").readlines()
    for line in lines:
        line = line.strip()
        k,md5 = line.split()
        print upload(md5+".mp3")
