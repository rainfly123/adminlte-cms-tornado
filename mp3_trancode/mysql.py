#!/usr/bin/env python
#coding:utf-8
import pymysql
import datetime
import os

def InsertResource(course_id, duration, file_size, file_name, file_format, file_order,
                            file_text, file_type, file_md5, create_time, download_url, description,
                            image_url, play_param, upload_account_id):
    conn = pymysql.connect(
    host="120.76.190.105",
    user="root",
    password= "123456",
    database="smartheadset",
    charset="utf8")
 
    cursor = conn.cursor() 
    sql = """insert into sh_resource_file (course_id, duration, file_size, file_name, file_format, file_order,\
          file_text, file_type, file_md5, create_time, download_url, description, image_url, play_param, \
          upload_account_id) values \
          (%s,%s,%s,"%s","%s",%s,"%s",%s,"%s","%s","%s", "%s", "%s", "%s", %s)""" %(course_id,
          duration, file_size, file_name, file_format, file_order,
                            file_text, file_type, file_md5, create_time, download_url, description,
                            image_url, play_param, upload_account_id)

   # print sql
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
   

def InsertCourse(course_name,
        course_category, 
        course_description, 
        image_url,
        course_count
        ):

    conn = pymysql.connect(
    host="120.76.190.105",
    user="root",
    password= "123456",
    database="smartheadset",
    charset="utf8")
    course_category = course_category[:100]
    course_description =  course_description[:1000]
    create_time = str(datetime.datetime.now()) 
    cursor = conn.cursor() 
    sql = 'insert into sh_course (course_name, course_category, \
           course_description,create_time, image_url, course_count) values \
           ("%s","%s","%s","%s","%s", %d)' %(course_name,
        course_category, 
        course_description, 
        create_time,
        image_url, course_count)

    print sql
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def getCourseID(course_name):

    conn = pymysql.connect(
    host="120.76.190.105",
    user="root",
    password= "123456",
    database="smartheadset",
    charset="utf8")
 
    cursor = conn.cursor() 
    sql = 'select course_id from sh_course where course_name= "%s"' %(course_name)
    cursor.execute(sql)
    c = cursor.fetchone()
    cursor.close()
    conn.close()
    return c[0]

def setCategory(course_id, course_category):

    conn = pymysql.connect(
    host="120.76.190.105",
    user="root",
    password= "123456",
    database="smartheadset",
    charset="utf8")
 
    cursor = conn.cursor() 
    sql = 'update sh_course set course_category = "%s" where course_id = "%d"' %(course_category, course_id)
 
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
   
def get():
    conn = pymysql.connect(
    host="120.76.190.105",
    user="root",
    password= "123456",
    database="smartheadset",
    charset="utf8")
 
    cursor = conn.cursor() 
    sql = 'select file_md5, course_id, download_url from sh_resource_file' 
 
    cursor.execute(sql)
    conn.commit()
    c = cursor.fetchall()
    cursor.close()
    conn.close()
    import os
    for m in c:
        print m[0], m[1], os.path.basename(m[2])
   
def set(key, md5):
    conn = pymysql.connect(
    host="120.76.190.105",
    user="root",
    password= "123456",
    database="smartheadset",
    charset="utf8")
    size = os.stat("./md5/"+md5 + ".mp3").st_size
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

