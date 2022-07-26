import peewee
from .base import BaseModel

class Team(BaseModel):
    id = peewee.IntegerField(unique=True, primary_key=True)
    name = peewee.TextField()
    rookie = peewee.IntegerField()