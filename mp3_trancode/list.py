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
bucket_name = 'smartheadset'

from qiniu import Auth
from qiniu import BucketManager
q = Auth(access_key, secret_key)
bucket = BucketManager(q)
# 前缀
prefix = None
# 列举条目
limit = None
# 列举出除'/'的所有文件以及以'/'为分隔的所有前缀
delimiter = None
# 标记
marker = None

eof = False
while eof == False:
    ret, eof, info = bucket.list(bucket_name, prefix, marker, limit, delimiter)
    marker = ret['marker']
    items = ret.get('items')
    if items is not None:
        for item in items:
            if item['mimeType'].count("audio") > 0:
                if item.has_key('md5') == False:
                    print item

