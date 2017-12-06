# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

tornado.options.define("port", default=8000, type=int, help="run server on the given port")
tornado.options.define("zhiying", default=["val1", "val2"], type=str, multiple=True, help="zhiying subject")


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello zhiying")


app = tornado.web.Application([
    (r"/", IndexHandler),
])


if __name__ == '__main__':
    # tornado.options.parse_command_line()
    tornado.options.parse_config_file("config.py")
    print(tornado.options.options.zhiying)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()
