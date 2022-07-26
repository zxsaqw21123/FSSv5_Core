import peewee
from .base import BaseModel
import datetime

class Team(BaseModel):
    id = peewee.IntegerField(unique=True, primary_key=True)
    name = peewee.TextField()
    rookie = peewee.IntegerField()

class Event(BaseModel):
    id = peewee.CharField(max_length = 10, unique=True, primary_key=True)
    name = peewee.TextField()
    location = peewee.TextField(null=True)
    startDate = peewee.DateField(default=datetime.date.today(), formats='%Y-%m-%d')
    endDate = peewee.DateField(default=datetime.date.today(), formats='%Y-%m-%d')
    teams = peewee.ManyToManyField(Team)