from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
from app import app, socketio, db

import json

from app.calc import SL

@socketio.on('SLCalc', namespace='/test')
def test_message(data):
	data['units_per_pip'] = 1e4
	data = dict((k,float(v)) for k,v in data.items())

	result = SL(**data)

	emit('sl_result',
		 result,
		 broadcast=False) 



