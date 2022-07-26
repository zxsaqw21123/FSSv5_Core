import asyncio
from multiprocessing.connection import wait
import os
import tornado.web
import tornado.ioloop

import peewee
from models.team import *
from handlers.team import TeamHandler

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
    # Create Database Table
    db = peewee.SqliteDatabase('data.sqlite')
    db.connect()
    db.create_tables([Team])
    db.close()

    settings = {
        'debug' : True,
        'static_path' : os.path.join(os.path.dirname(__file__) , "static") ,
        'template_path' : os.path.join(os.path.dirname(__file__) , "template") ,
    }

    application = tornado.web.Application([
        (r"/" , MainHandler),
        (r"/api/team/(\d*$)", TeamHandler),
    ] , **settings)
    application.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
