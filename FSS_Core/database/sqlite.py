import peewee

class Repository:
    def __init__(self, obj):
        self.obj = obj()

    def create(self, **data):
        return self.obj.create(**data)

    def bulk_create(self, data):
        self.obj.insert_many(data).execute()

    def update(self, **data):
        return self.obj.replace(**data).execute()

    def delete(self, id):
        return self.obj.delete_by_id(id)

    def get(self, id):
        try:
            res = self.obj.get_by_id(id).__data__
        except:
            query = self.obj.select()
            res = [q.__data__ for q in query]
        return res
    
    def all(self):
        return self.obj.filter()