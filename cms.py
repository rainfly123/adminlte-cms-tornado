#!/usr/bin/env python
#coding:utf8
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import time
import mysql
import vfs

from tornado.options import define, options
define("port", default=9180, help="run on the given port", type=int)

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MdataHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        #self.write("Hello, world")
        #self.redirect("/static/adminlte/starter.html")
        columns_name, data = mysql.Get("sh_course")
        names = ["ID","课程名称", "出版社", "作者","分类","简介","描述","创建时间","免费","图标","总节数","类型"]
 
        self.render(template_name = "mdata.html", columns = names, rows = data)

class NdataHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        #self.write("Hello, world")
        #self.redirect("/static/adminlte/starter.html")
        columns_name, data = mysql.Get("sh_resource_file")
        names = ["课件ID","课程ID", "时长", "大小","名称","格式","次序","文字版","类型","MD5","创建时间","URL",
                "描述","图标","参数","上传者"]
 
        self.render(template_name = "ndata.html", columns = names, rows = data)
 

class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        #self.write("Hello, world")
        #self.redirect("/static/adminlte/starter.html")
        Free, Used, Ration =  vfs.GetUsage()
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
