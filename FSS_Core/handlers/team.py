from .base import BaseHandler
from http import HTTPStatus
from database.sqlite import Repository
from models.team import Team
import json

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

        