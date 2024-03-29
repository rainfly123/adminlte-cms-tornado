#!/usr/bin/env python
#coding:utf-8
import sys;
reload(sys);
sys.setdefaultencoding("utf8")
from qiniu import Auth
from qiniu import put_file, etag
import qiniu.config
import uuid
import base64
import os
URL = "https://resource.qctchina.top"
access_key = 'pkTzM_Eu4vrIYJDuh4u5psLAWzycH7nozlWU2z'
secret_key = 'P6JLYU87Oxc8cDjL5SWL6Ajfg1Nonm6NH0TN'

q = Auth(access_key, secret_key)
bucket_name = 'smartheadset'

def upload(localfile):
    key = str(uuid.uuid1())
    code = base64.b64encode(key)
    suffix = os.path.splitext(localfile)[1]
    keyname = "".join([code, suffix])

    token = q.upload_token(bucket_name, keyname, 3600*100)
    ret, info = put_file(token, keyname, localfile)
    if ret['hash'] == etag(localfile):
        return os.path.join(URL, keyname)
    return None

if __name__ =='__main__':
    localfile = 'upload/英语能力_词汇-新闻热词/资源/新闻热词_Sino-US relations.mp3'
    print upload(localfile)
