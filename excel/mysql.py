#!/usr/bin/env python
#coding:utf-8
import pymysql
import datetime

def InsertResource(course_id, duration, file_size, file_name, file_format, file_order,
                            file_text, file_type, file_md5, create_time, download_url, description,
                            image_url, play_param, upload_account_id):
    conn = pymysql.connect(
    host="localhost",
    user="root",
    password= "1",
    database="smartheadset",
    charset="utf8")
 
    cursor = conn.cursor() 
    sql = 'insert into sh_resource_file (course_id, duration, file_size, file_name, file_format, file_order,\
          file_text, file_type, file_md5, create_time, download_url, description, image_url, play_param, \
          upload_account_id) values \
          (%s,%s,%s,"%s","%s",%s,"%s",%s,"%s","%s","%s", "%s", "%s", "%s", %s)' %(course_id,
          duration, file_size, file_name, file_format, file_order,
                            file_text, file_type, file_md5, create_time, download_url, description,
                            image_url, play_param, upload_account_id)

    print sql
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
    host="localhost",
    user="root",
    password= "1",
    database="smartheadset",
    charset="utf8")
 
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
    host="localhost",
    user="root",
    password= "1",
    database="smartheadset",
    charset="utf8")
 
    cursor = conn.cursor() 
    sql = 'select course_id from sh_course where course_name= "%s"' %(course_name)
    print sql
    cursor.execute(sql)
    c = cursor.fetchone()
    cursor.close()
    conn.close()
    return c[0]
 
   
