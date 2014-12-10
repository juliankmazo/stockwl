from google.appengine.ext import ndb


class BaseModel(ndb.Model):
    """
    This class is the Base Model for any entity that will be created in the ndb database.
    All entities should have these two properties, which are automatically added.
    """
    created = ndb.DateTimeProperty(auto_now_add=True)  # This is the timestamp of the creation date of the entity.
    timestamp = ndb.DateTimeProperty(auto_now=True)  # This is the timestamp that gives information about the last modification of the entity.
