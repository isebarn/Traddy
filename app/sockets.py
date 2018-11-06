from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
from app import app, socketio, db

import json

from app.calc import SL

from app.models import Pairs


@socketio.on('SLCalc', namespace='/test')
def test_message(data):
	data['units_per_pip'] = 1e4
	data = dict((k,float(v)) for k,v in data.items())

	result = SL(**data)

	emit('sl_result',
		 result,
		 broadcast=False) 

@socketio.on('Order', namespace='/test')
def test_message(data):

	emit('order',
		 data,
		 broadcast=False)	



@socketio.on('request_ui_data', namespace='/test')
def test_message(data):
	pairs = Pairs.query.all()

	result = [{'id': pair.pair_id, 'pair': pair.pair, 'units_per_pip': float(pair.units_per_pip_usd), 'comission': float(pair.comission)} for pair in pairs]
	print(result)
	emit('ui_data',
		 json.dumps(result),
		 broadcast=False)	