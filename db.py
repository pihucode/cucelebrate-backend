from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    month = db.Column(db.Integer, nullable=True)
    day = db.Column(db.Integer, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    time = db.Column(db.String, nullable=True)
    descr = db.Column(db.String, nullable=True) #block of text
    location = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    interest = db.Column(db.Integer, nullable=True) # number of people who favorited this event

    def __init__(self, **kwargs):
        self.title = kwargs.get('title', '')
        self.month = kwargs.get('month', '')
        self.day = kwargs.get('day', '')
        self.year = kwargs.get('year', '')
        self.descr = kwargs.get('descr', '')
        self.location = kwargs.get('location', '')
        self.category = kwargs.get('category', '')
        self.interest = kwargs.get('interest', 0)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'month': self.month,
            'day': self.day,
            'year': self.year,
            'time': self.time,
            'descr': self.descr,
            'location': self.location,
            'category': self.category,
            'interest': self.interest,
        }
