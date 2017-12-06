# coding:utf-8

import json
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
from tornado.web import RequestHandler
from tornado.options import options, define


define("port", default=8000, type=int, help="run server on the port")


class IndexHandler(RequestHandler):
    # def get(self):
    #     stu = {
    #         "name": "wuyuw",
    #         "age": 24,
    #         "gender": "male"
    #     }
    #     stu = json.dumps(stu)
    #     self.write(stu)
    #     self.set_header("Content-Type", "application/json;charset=UTF-8")

    def set_default_headers(self):
        print("执行set_default_headers")
        self.set_header("Content-Type", "application/json;charset=UTF-8")
        self.set_header("python", "hello")


    def get(self):
        print("执行get()")
        stu = {
            "name": "wuyuw",
            "age": 24,
            "gender": "male"
        }
        stu = json.dumps(stu)
        self.write(stu)
        self.set_header("python", "wuyuw")

    def post(self):
        print("执行post()")
        stu = {
            "name": "wuyuw",
            "age": 24,
            "gender": "male"
        }
        stu = json.dumps(stu)
        self.write(stu)


class Err404Handler(RequestHandler):
    def get(self):
        self.write("hello python")
        self.set_status(404)


class Err210Handler(RequestHandler):
    def get(self):
        self.write("hello python")
        self.set_status(210, "python error")


class Err211Handler(RequestHandler):
    def get(self):
        self.write("hello python")
        self.set_status(211)


class UserHandler(RequestHandler):
    """/user"""
    def get(self):
        self.redirect("/")


class SendErrHandler(RequestHandler):
    """/send_err"""
    def get(self):
        self.write("send_err")
        self.send_error(404, content="404错误")
        # self.write("over")


class WriteErrHandler(RequestHandler):
    """/write_err"""
    def post(self):
        err_code = self.get_argument("code", None)
        err_title = self.get_argument("title", "")
        err_content = self.get_argument("content", "")
        if err_code:
            self.send_error(err_code, title=err_title, content=err_content)
        else:
            self.write("write_err")

    def write_error(self, status_code, **kwargs):
        self.write("<h1>出错啦</h1>")
        self.write("<h3>错误类型：%s</h3>" % kwargs["title"])
        self.write("<h3>错误详情：%s</h3>" % kwargs["content"])


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/404", Err404Handler),
        (r"/210", Err210Handler),
        (r"/211", Err211Handler),
        (r"/user", UserHandler),
        (r"/send_err", SendErrHandler),
        (r"/write_err", WriteErrHandler)
    ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

