# coding:utf-8


import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
from tornado.web import RequestHandler
from tornado.options import define, options


define("port", default=8000, type=int, help="runserver on the port")


class SubjectCityHandler(RequestHandler):
    def get(self, subject, city):
        self.write("subjcet: %s<br/>City: %s" % (subject, city))


class SubjectDateHandler(RequestHandler):
    def get(self, subject, date):
        self.write("subject: %s<br/>Date: %s" % (subject, date))


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/sub-city/(.+)/([a-z]+)", SubjectCityHandler),
        (r"/sub-date/(?P<subject>.+)/(?P<date>\d+)", SubjectDateHandler)
    ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
