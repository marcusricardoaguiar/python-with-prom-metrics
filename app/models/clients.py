from .database import db

class Client(db.Model):

    id   = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'id': self.id, 'name': self.name}
