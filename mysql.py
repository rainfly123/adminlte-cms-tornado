#!/usr/bin/env python
import pymysql

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

if __name__ == "__main__":
    ncolumns , results = Get("sh_course")
    print ncolumns, results

    ncolumns , results = Get("sh_resource_file")
    print ncolumns, results
