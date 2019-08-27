#!/usr/bin/env python
#coding:utf-8
import os
import sys
import xlrd
import mysql
import qiniusdk



if __name__ =='__main__':

    if len(sys.argv) < 2:
        sys.exit(-1)

    book = xlrd.open_workbook(sys.argv[1])
    sheets = book.sheet_names()
    for sheet in sheets:
        csheet = book.sheet_by_name(sheet)
        #for x in xrange(csheet.nrows):
        #for x in [i + 1 for i in xrange(csheet.nrows)]:
        #    for col in csheet.row_values(x):
        #        print col
        #break

        # 1-n row, 6 col 课程标签
        course_category = " ".join(csheet.col_values(6)[1:])
        # 1 row, 5 col  课程描述
        #print csheet.cell_value(1,5)
        course_description =  csheet.cell_value(1, 5)
        course_count = csheet.nrows - 1
        course_name = sheet
        localfile = os.path.join("upload", course_name, u"图片",u"介绍.png")
        image_url = qiniusdk.upload(localfile)
        if image_url != None:
            mysql.InsertCourse(course_name, course_category[:49], course_description, image_url, course_count)


