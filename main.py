#!/usr/bin/env python
import os
import jinja2
import webapp2

from models import Message


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        message1 = Message.query().order(-Message.created).fetch()

        params = {"message": message1}

        self.render_template("index.html", params)


class MsgsentHandler(BaseHandler):
    def post(self):
        name = self.request.get("name")
        msg = self.request.get("msg")

        message2 = Message(name=name, msg=msg)
        message2.put()

        self.render_template("msgsent.html")




app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/msgsent', MsgsentHandler),
], debug=True)
