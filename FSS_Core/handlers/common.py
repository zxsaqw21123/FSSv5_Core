from .base import BaseHandler
from http import HTTPStatus
from database.repository import *
from models.common import Team, Event
import json
from datetime import datetime

class TeamHandler(BaseHandler):
    def prepare(self):
        self.db = Repository(Team)
        pass

    def get(self, id=None):
        data = self.db.get(id)
        self.write_response(HTTPStatus.OK, data, "get Team!")

    def post(self, id):
        self.args = json.loads(self.request.body)
        try:
            newId = self.db.create(**self.args)
        except:
            self.send_error(HTTPStatus.BAD_REQUEST)
        else:
            self.redirect(f"/api/team/{newId}")

    def put(self, id):
        self.args = json.loads(self.request.body)
        newId = self.db.update(**self.args)
        if newId != id:
            self.db.delete(id)
        self.redirect(f"/api/team/{newId}")

    def delete(self, id):
        self.db.delete(id)
        self.redirect(f"/api/team/")

        
class EventHandler(BaseHandler):
    def prepare(self):
        self.db = Repository(Event)
        pass

    def get(self, id=None):
        data = self.db.get(id)
        print(list(data.teams))
        self.write_response(HTTPStatus.OK, data, "get Event!")

    def post(self, id):
        self.args = json.loads(self.request.body)
        newId = self.db.create(**self.args)
        self.redirect(f"/api/event/{newId}")

    def put(self, id):
        self.args = json.loads(self.request.body)
        newId = self.db.update(**self.args)
        if newId != id:
            self.db.delete(id)
        self.redirect(f"/api/event/{newId}")

    def delete(self, id):
        self.db.delete(id)
        self.redirect(f"/api/event/")

        