#!/usr/bin/env python
#coding:utf8
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import time
import mysql
import utils 
import uuid

from tornado.options import define, options
define("port", default=9180, help="run on the given port", type=int)

DNS="http://127.0.0.1:9180/"
PATH="/home/rain/temp/"

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class minputHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        self.render(template_name = "minput.html", user=name)
    def post(self):
        course_name = self.get_argument("course_name")
        publisher = self.get_argument("publisher")
        course_author = self.get_argument("course_author")
        course_category = self.get_argument("course_category")
        course_abstract = self.get_argument("course_abstract")
        course_description = self.get_argument("course_description")
        course_count = self.get_argument("course_count")
        free = self.get_argument("free")

        files = self.request.files
        mylogo = str(uuid.uuid1())
        img_files = files.get("logo")
        #print(img_files,'=========================================')
        if img_files:
            img_file = img_files[0]["body"] 
            ext = os.path.splitext(img_files[0]['filename'])[1]
            mylogo += ext
            with open(os.path.join(PATH, mylogo), 'wb') as f:
                f.write(img_file)

        mymp3 = str(uuid.uuid1())
        mp3_files = files.get("mp3")
        #print(mp3_files,'=========================================')
        if mp3_files:
            mp3_file = mp3_files[0]["body"] 
            ext = os.path.splitext(mp3_files[0]['filename'])[1]
            mymp3 += ext
            with open(os.path.join(PATH, mymp3), 'wb') as f:
                f.write(mp3_file)


class MdataHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        #self.write("Hello, world")
        #self.redirect("/static/adminlte/starter.html")
        columns_name, data = mysql.Get("sh_course")
        names = ["ID","课程名称", "出版社", "作者","分类","简介","描述","创建时间","免费","图标","总节数","类型"]
 
        self.render(template_name = "mdata.html", user=name, columns = names, rows = data)

class NdataHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        #self.write("Hello, world")
        #self.redirect("/static/adminlte/starter.html")
        columns_name, data = mysql.Get("sh_resource_file")
        names = ["课件ID","课程ID", "时长", "大小","名称","格式","次序","文字版","类型","MD5","创建时间","URL",
                "描述","图标","参数","上传者"]
 
        self.render(template_name = "ndata.html", user=name, columns = names, rows = data)
 

class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        #self.write("Hello, world")
        #self.redirect("/static/adminlte/starter.html")
        Free, Used, Ration =  utils.GetUsage()
        self.render(template_name = "index.html", user=name, free=Free, used=Used)
        """
        self.render(
            template_name = "index.html",
            title = "Hi " + name,
            header="Books that are great",
            books=[
                "Learning Python",
                "Programming Collective Intelligence",
                "Restful Web Services"
            ]
        )
        """

class LoginHandler(BaseHandler):
    def get(self):
        self.render(
            template_name = "login.html",
        )
        #self.write('<html><body><form action="/login" method="post">'
        #           'Name: <input type="text" name="name">'
        #           'Password: <input type="text" name="password">'
        #           '<input type="submit" value="Sign in">'
        #           '</form></body></html>')

    def post(self):
        name = self.get_argument("name")
        password = self.get_argument("password")
        if name == "admin" and password == "xiechc":
            self.set_secure_cookie("user", name)
            self.redirect("/")
        else:
            self.redirect("/login")

def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
            (r"/", MainHandler),
            (r"/mdata", MdataHandler),
            (r"/ndata", NdataHandler),
            (r"/login", LoginHandler),
            (r"/minput", minputHandler),
        ],
        template_path = os.path.join(os.path.dirname(__file__), "templates"),
        static_path = os.path.join(os.path.dirname(__file__), "static"),
        debug = True,
        cookie_secret="xiechc@gmail.com",
        login_url="/login")

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
