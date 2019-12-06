#!/usr/bin/env python
#coding:utf-8
import pymysql
import datetime
import os

   
def gset(key, md5):
    conn = pymysql.connect(
    host="120.76.190.105",
    user="root",
    password= "123456",
    database="smartheadset",
    charset="utf8")
    size = os.stat("./new/"+md5 + ".mp3").st_size
    cursor = conn.cursor() 
    sql = 'update sh_resource_file set file_md5="%s" where download_url like "%%%s"' %(md5, key)
    cursor.execute(sql)
    conn.commit()

    sql = 'update sh_resource_file set file_size=%s where download_url like "%%%s"' %(size, key)
    cursor.execute(sql)
    conn.commit()

    sql = 'update sh_resource_file set download_url="https://resource.qctchina.top/%s.mp3"\
 where download_url like "%%%s"' %(md5, key)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


lines=open('aaa', 'r').readlines()
for line in lines:
    line = line.strip()
    key, md5=line.split() 
    gset(key, md5)

