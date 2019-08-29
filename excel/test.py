#!/usr/bin/env python
#coding:utf-8
import os
import sys
import xlrd
import datetime
import utils
import mysql
import re



def Course(filename):
    book = xlrd.open_workbook(filename)
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
        localfile = os.path.join(course_name, u"图片",u"介绍.png")
        if os.access(localfile, os.R_OK) != True:
            print u"!!!!没有课程封面:%s"%localfile

def Resourse(filename):
    create_time = str(datetime.datetime.now()) 
    book = xlrd.open_workbook(filename)
    sheets = book.sheet_names()
    for sheet in sheets:
        csheet = book.sheet_by_name(sheet)
        course_id = mysql.getCourseID(sheet)
        for x in [i + 1 for i in xrange(csheet.nrows - 1)]:
             file_name = csheet.cell_value(x,1)
             description = csheet.cell_value(x,2)
             if len(description) > 0:
                 description = re.escape(description)
             mp3filename = csheet.cell_value(x,3)
             file_order = x 
             file_format = "mp3"
             play_param = ""
             upload_account_id = 1
             file_text = ""
             file_type = 1

             localpath = os.path.join(sheet, u"资源")  
             check = u"%s.mp3"%(mp3filename)
             file_path = os.path.join(localpath, check)
             print file_path
             if os.access(file_path, os.R_OK) == True:
                 duration = utils.GetDuration(file_path)
                 file_md5 = utils.GetMd5(file_path)
                 file_size = utils.GetSize(file_path)
                 pic_path = checkPicName(sheet, mp3filename, x)
                 if pic_path == None:
                     print u"!!!!!没有图片文件:《%s》-->(%s)=(%s)====="%(sheet, file_name, pic_path)
             else:
                print u"!!!!!没有资源文件:《%s》-->(%s)=%d====="%(sheet, file_name, x)
                continue


def checkPicName(course_name, filename, index):
        localpath = os.path.join(course_name, u"图片")  
        check1 = u"描述_%d.png"%(index)
        file_path = os.path.join(localpath, check1)
        if os.access(file_path, os.R_OK) == True:
            return file_path 
        check2 = u"描述_%d.jpg"%(index)
        file_path = os.path.join(localpath, check2)
        if os.access(file_path, os.R_OK) == True:
            return file_path 
        check3 = u"%s.png"%(filename)
        file_path = os.path.join(localpath, check3)
        if os.access(file_path, os.R_OK) == True:
            return file_path 

        check4 = u"%s.jpg"%(filename)
        file_path = os.path.join(localpath, check4)
        if os.access(file_path, os.R_OK) == True:
            return file_path 

        check5 = u"介绍.png"
        file_path = os.path.join(localpath, check5)
        if os.access(file_path, os.R_OK) == True:
            return file_path 

        check6 = u"介绍.jpg"
        file_path = os.path.join(localpath, check6)
        if os.access(file_path, os.R_OK) == True:
            return file_path 

if __name__ =='__main__':
    if len(sys.argv) < 2:
        print "   {0} [excelfile] [1/2]\n    excel \
        file's full path\n    1 create course, 2 create all resource".format(sys.argv[0])
         
        sys.exit(-1)

    if sys.argv[2] == "1":
        Course(sys.argv[1])
    elif sys.argv[2] == "2":
        Resourse(sys.argv[1])

