#!/usr/bin/env python
import tornado.ioloop
import tornado.web

# generics
class User(object):
    username = ""
    password = ""

#oauth2
class Oauth2Client(object):
    user = User
    client_id = ""

class Oauth2Token(object):
    client = Oauth2Token
    user = User

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
# tornadoauth.addOauth2handlers(application)
# This should test adding the handlers to the application
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()



