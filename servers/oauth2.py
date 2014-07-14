# codeing: utf-8
import tornado.web
from oauthlib.oauth2 import WebApplicationServer
from ..utils import extract_params

class Oauth2Handler(tornado.web.RequestHandler):
    def get_current_user():
        pass
        # stub, will return oauth identiier

class Oauth2Server(object):
    """ Oauth2Server modified the passed application object with everything
    required to act as an Oauth2 server. It will add all the necessary
    handlers and routes to the application.
    
    You also need to create your own requestValidator as defined in the
    oauthlib docs:
        http://oauthlib.readthedocs.org/en/latest/oauth2/validator.html
    """

    def __init__(self, application=None validator=None, server=None):
        if not application:
            raise RuntiumeError('Must pass an instance of tornado.application')
        else:
            self.application = application
        if not validator:
            raise RuntiumeError('Must pass a validator')
        if not server:
            server = WebApplicationServer
        application.oauth2Server = server(validator)

class AuthorizationViewHandler(tornado.web.requestHandler):
    def get(self):
        uri, method, body, headers = extract_params(self.request)
       

            
    

