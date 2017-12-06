# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web


# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write('<html><body><form action="/" method="post">'
#                    '<input type="text" name="message">'
#                    '<input type="submit" value="Submit">'
#                    '</form></body></html>')
#
#     def post(self):
#         self.set_header("Content_Type", "text/plain")
#         # raise tornado.web.HTTPError(403)
#         self.write("You wrote " + self.get_argument("message"))
#         print(self.request.arguments.get("message"))

# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         if not self.get_cookie("mycookie"):
#             self.set_cookie("mycookie", "myvalue")
#             self.write("Your cookie was not set yet")
#         else:
#             self.write("Your cookie was set!")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie("mycookie"):
            self.set_secure_cookie("mycookie", "myvalue")
            self.write("Your cookie was not set Yet")
        else:
            self.write("Your cookie was set")


class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)


class TemplateHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("template.html", title="My title", items=items)


application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/story/([0-9]+)', StoryHandler),
    (r'/template', TemplateHandler),
], cookie_secret="tornado_web")

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
