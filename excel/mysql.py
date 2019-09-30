#!/usr/bin/env python
#coding:utf-8
import pymysql
import datetime

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
   
