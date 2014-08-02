#!/usr/bin/env python
import uuid
import tornado.web
import tornado.ioloop
from oauthlib.oauth2 import RequestValidator, WebApplicationServer

# generic user model
class User(object):
    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password
        self.client = None

#oauth2 client model
class Oauth2Client(object):
    def __init__(self, user=None, client_id=None):
        self.user = user
        self.id = unicode(uuid.uuid4()) # client id should be unicode

#oauth2 token model
class Oauth2Token(object):
    def __init__(self, client=None, user=None, token=None, refreshToken=None)
        self.client = client
        self.user = user
        self.token = unicode(uuid.uuid4()) 
        self.refreshToken = unicode(uuid.uuid4()) 


users = [
        User(name="test1", password="t123"),
        User(name="test2", password="t321"),
        ]

oauth2Tokens = []
oauth2Clients = []

def oauth2ClientGetter(id):
    for client in clients:
        if client.id == id:
            return client
    return None

def oauth2ClientSetter(user = None):
    clients.append(Client(user=user))


class MainHandler(tornado.web.RequestHandle):
    """ Just a helloworld handler taken from the offical tornado docs to act
    as a placeholder while I start to write tests."""
    def get(self):
        self.write("Hello, world")

def main():
    """ The tests module should start a web server capable of providing acting
    as an oauth server. Since oauth depends on end points the oauth modules
    should add handlers to the application. 

    Included should be hooks for authentication, but it should be written to
    support various forms of authentication.
    
    The tests module should be written to be able to handle any type of server
    so this may all be rewritten to either stop and create new servers or to
    edit the application on the fly. Haven't sorted that out yet."""


    application = tornado.web.Application([
        (r"/", MainHandler),
        ])

    application.oauth2Server = tornadoauth.oauth2Server()

# This should test adding the handlers to the application
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()



