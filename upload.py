# coding:utf-8


import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
from tornado.options import options, define
from tornado.web import RequestHandler


define("port", default=8000, type=int, help="run server on the port")


class UploadHandler(RequestHandler):
    def post(self):
        files = self.request.files
        print(files)
        img_files = files.get('img')
        if img_files:
            print(img_files[0]["filename"])
            img_file = img_files[0]["body"]
            with open("./img01.jpg", "wb") as f:
                f.write(img_file)
        self.write("OK")


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/upload", UploadHandler),
    ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
