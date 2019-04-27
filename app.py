import json
from flask import Flask, request
from db import db, Event

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def root():
    return 'Hello world!'

# Create an event
@app.route('/api/events/', methods=['POST'])
def create_event():
    post_body = json.loads(request.data)
    event = Event(
        title = post_body.get('title'),
        date_posted = post_body.get('date_posted'),
        time = post_body.get('time'),
        descr = post_body.get('descr'),
        location = post_body.get('location'),
        category = post_body.get('category'),
    )
    db.session.add(event)
    db.session.commit()
    return json.dumps({'success': True, 'data': event.serialize()}), 201

# Get all events
@app.route('/api/events/')
def get_events():
    events = Event.query.all()
    res = {'success': True, 'data': [event.serialize() for event in events]}
    return json.dumps(res), 200

# Get a specific event
@app.route('/api/event/<int:event_id>/')
def get_event(event_id):
    event = Event.query.filter_by(id=event_id).first()
    if event is None:
        return json.dumps({'success': False, 'error': 'Event not found.'}), 404
    return json.dumps({'success': True, 'data': event.serialize()}), 200

# Edit an event
@app.route('/api/event/<int:event_id>/', methods=['POST'])
def edit_event(event_id):
    event = Event.query.filter_by(id=event_id).first()
    if event is not None:
        post_body = json.loads(request.data)
        event.title = post_body.get('title', event.title)
        event.descr = post_body.get('descr', event.descr)
        event.time = post_body.get('time', event.time)
        event.location = post_body.get('location', event.location)
        db.session.commit()
        return json.dumps({'success': True, 'data': event.serialize()}), 200
    return json.dumps({'success': False, 'error': 'Event not found.'}), 404

# Delete a specific event
@app.route('/api/event/<int:event_id>/', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.filter_by(id=event_id).first()
    if event is not None:
        db.session.delete(event)
        db.session.commit()
        return json.dumps({'success': True, 'data': event.serialize()}), 200
    return json.dumps({'success': False, 'error': 'Event not found.'}), 404

# Update event interest
# Needs a unique route - solved
@app.route('/api/event/<int:event_id>/interest/<string:update>/', methods=['POST'])
def increment_interest(event_id, update):
    event = Event.query.filter_by(id=event_id).first()
    if event is not None:
        # checks route argument
        if update == "increment":
            event.interest += 1

        elif update == "decrement":
            # interest should not go below 0
            if event.interest > 0:
                event.interest -= 1

        db.session.commit()
        return json.dumps({'success': True, 'data': event.serialize()}), 200
    return json.dumps({'success': False, 'error': 'Event not found.'}), 404

# Get all events of a specific category
@app.route('/api/events/<string:category_type>/')
def get_events_of_category(category_type):
    events = Event.query.filter_by(category=category_type)
    res = {'success': True, 'data': [event.serialize() for event in events]}
    return json.dumps(res), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)