import peewee

class BaseModel(peewee.Model):
    class Meta:
        database = peewee.SqliteDatabase('data.sqlite')


