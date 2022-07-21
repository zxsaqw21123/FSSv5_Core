import asyncio
from multiprocessing.connection import wait
import os
import tornado.web
import tornado.ioloop

from app.api.handler import *

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello , SELECT\n")

    def post(self):
        self.write("hello , ADD\n")

    def put(self):
        self.write("hello , UPDATE\n")

    def delete(self):
        self.write("hello , DELETE\n")

async def main():
    settings = {
        'debug' : True,
        'static_path' : os.path.join(os.path.dirname(__file__) , "static") ,
        'template_path' : os.path.join(os.path.dirname(__file__) , "template") ,
    }

    application = tornado.web.Application([
        (r"/" , MainHandler),
        (r"/api/event", EventHandler),
    ] , **settings)
    application.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
