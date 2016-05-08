#!/usr/bin/env python

import os
import jinja2
import webapp2
from google.appengine.api import users

from emoteicons import emoteicon
from escape import escape_html
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

        user = users.get_current_user()
        if user:
            if users.is_current_user_admin():
                admin = True
                params["admin"] = admin
            logged_in = True
            logout_url = users.create_logout_url("/")
            params["logged_in"] = logged_in
            params["user"] = user
            params["logout_url"] = logout_url
        else:
            logged_in = False
            login_url = users.create_login_url("/")
            params["logged_in"] = logged_in
            params["user"] = user
            params["login_url"] = login_url

        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        message1 = Message.query().order(-Message.created).fetch()

        params = {"message": message1}

        self.render_template("index.html", params)


class MsgsentHandler(BaseHandler):
    def post(self):
        msg = self.request.get("msg")
        name = users.get_current_user().nickname()

        msg = escape_html(msg)

        msg = emoteicon(msg)

        message2 = Message(msg=msg, name=name)
        message2.put()

        return self.redirect_to("home")


class MsgDelete(BaseHandler):
    def get(self, msg_id):
        msg = Message.get_by_id(int(msg_id))

        params = {"msg": msg}

        self.render_template("delete_msg.html", params)

    def post(self, msg_id):
        msg = Message.get_by_id(int(msg_id))

        msg.key.delete()

        return self.redirect_to("home")


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="home"),
    webapp2.Route('/msgsent', MsgsentHandler),
    webapp2.Route('/<msg_id:\d+>/delete', MsgDelete),
], debug=True)
