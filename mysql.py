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
   


if __name__ == "__main__":
    ncolumns , results = Get("sh_course")
    print ncolumns, results

    ncolumns , results = Get("sh_resource_file")
    print ncolumns, results
