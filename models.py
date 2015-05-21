from google.appengine.ext import ndb


class Message(ndb.Model):
    msg = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    name = ndb.StringProperty()
