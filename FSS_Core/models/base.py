import peewee

class BaseModel(peewee.Model):
    class Meta:
        database = peewee.SqliteDatabase('data.sqlite')

class MemModel(peewee.Model):
    class Meta:
        database = peewee.SqliteDatabase(':memory:')