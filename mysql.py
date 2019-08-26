#!/usr/bin/env python
import pymysql
import datetime

def Get(table_name):
    conn = pymysql.connect(
    host="localhost",
    user="root",
    password= "1",
    database="smartheadset",
    charset="utf8")
 
 
    cursor = conn.cursor() 
    sql = "select * from " + table_name
    nsql=" select column_name from information_schema.columns where  table_name = '%s'"%(table_name)
 
    cursor.execute(sql)
    results = cursor.fetchall()

    cursor.execute(nsql)
    mresults = cursor.fetchall()
    nresults = [var[0] for var in mresults]
    cursor.close()
    conn.close()
    return nresults, results

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
        publisher, 
        course_author,
        course_category, 
        course_abstract,
        course_description, 
        course_free, 
        image_url,
        course_count, 
        course_type):

    conn = pymysql.connect(
    host="localhost",
    user="root",
    password= "1",
    database="smartheadset",
    charset="utf8")
 
    create_time = str(datetime.datetime.now()) 
    cursor = conn.cursor() 
    sql = 'insert into sh_course (course_name, publisher,course_author,course_category, course_abstract,\
           course_description,create_time, course_free, image_url, course_count, course_type) values \
           ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' %(course_name,
        publisher, 
        course_author,
        course_category, 
        course_abstract,
        course_description, 
        create_time,
        course_free, image_url, course_count, course_type)
    print sql
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
   
def GetCourseNumber():
    conn = pymysql.connect(
    host="localhost",
    user="root",
    password= "1",
    database="smartheadset",
    charset="utf8")
 
 
    cursor = conn.cursor() 
    sql="select count(course_id) from sh_course"
 
    cursor.execute(sql)
    results = cursor.fetchone()

    cursor.close()
    conn.close()
    return results[0]

def GetResourceNumber():
    conn = pymysql.connect(
    host="localhost",
    user="root",
    password= "1",
    database="smartheadset",
    charset="utf8")
 
 
    cursor = conn.cursor() 
    sql="select count(resource_file_id) from sh_resource_file"
 
    cursor.execute(sql)
    results = cursor.fetchone()

    cursor.close()
    conn.close()
    return results[0]




if __name__ == "__main__":
    ncolumns , results = Get("sh_course")
    print ncolumns, results

    ncolumns , results = Get("sh_resource_file")
    print ncolumns, results
    print GetCourseNumber()
    print GetResourceNumber()
