from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    day = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    time = db.Column(db.String, nullable=False)
    descr = db.Column(db.String, nullable=True) #block of text
    location = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    interest = db.Column(db.Integer, nullable=True) # number of people who favorited this event
    image_url = db.Column(db.String, nullable=False)

    def __init__(self, **kwargs):
        self.title = kwargs.get('title', '')
        self.month = kwargs.get('month', '')
        self.day = kwargs.get('day', '')
        self.year = kwargs.get('year', '')
        self.descr = kwargs.get('descr', 'No description has been provided.')
        self.location = kwargs.get('location', '')
        self.category = kwargs.get('category', '')
        self.interest = kwargs.get('interest', 0)
        self.image_url = kwargs.get('image_url', '')

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
            'image_url': self.image_url,
        }
