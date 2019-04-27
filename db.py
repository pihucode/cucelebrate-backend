from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False) #event title 50 chars max
    date_posted = db.Column(db.Integer, nullable=False) # should automatically detect date
    time = db.Column(db.Integer, nullable=True)
    descr = db.Column(db.String, nullable=True) #block of text
    location = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    interest = db.Column(db.Integer, nullable=True) # number of people who favorited this event

    def __init__(self, **kwargs):
        self.title = kwargs.get('title', '')
        self.date_posted = kwargs.get('date_posted', '')
        self.time = kwargs.get('time', '')
        self.descr = kwargs.get('descr', '')
        self.location = kwargs.get('location', '')
        self.category = kwargs.get('category', '')
        self.interest = kwargs.get('interest', 0)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'date_posted': self.date_posted,
            'time': self.time,
            'descr': self.descr,
            'location': self.location,
            'category': self.category,
            'interest': self.interest,
        }
