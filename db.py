from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False) #event title
    date_posted = db.Column(db.Integer, nullable=False) #automatically detect date
    descr = db.Column(db.String, nullable=False) #block of text
    location = db.Column(db.String, nullable=False)

    def __init__(self, **kwargs):
        self.title = kwargs.get('title', 'Unnamed')
        self.date_posted = kwargs.get('date_posted', '')
        self.descr = kwargs.get('descr', 'No decription available')
        self.location = kwargs.get('location', 'Location not specified')

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'date_posted': self.date_posted,
            'descr': self.descr,
            'location': self.location,
        }
