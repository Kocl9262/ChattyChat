from google.appengine.ext import ndb


class Message(ndb.Model):
    name = ndb.StringProperty()
    msg = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
