from tornado.web import RequestHandler
from .model import *

class EventHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, PUT, DELETE")
        self.set_header("Content-Type", "application/json")

    def get(self):
        self.write("Hello, get Event!")
