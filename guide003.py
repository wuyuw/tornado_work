# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import options, define
from tornado.web import url, RequestHandler

define("port", default=8000, type=int, help="run server on the port")


class IndexHandler(RequestHandler):
    def get(self):
        python_url = self.reverse_url("python_url")
        self.write('<a href="%s">python</a>' % python_url)


class PythonHandler(RequestHandler):
    def initialize(self, subject):
        self.subject = subject

    def get(self):
        self.write(self.subject)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/cpp", PythonHandler, {"subject": "c++"}),
        url(r"/python", PythonHandler, {"subject": "python"}, name="python_url")
    ],
    debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
