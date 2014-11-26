from google.appengine.ext import ndb


class BaseModel(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    timestamp = ndb.DateTimeProperty(auto_now=True)
