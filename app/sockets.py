from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
from app import app, socketio, db

import json

from app.calc import SL

from app.models import Pairs

from urllib.parse import urlencode, quote_plus
import urllib.request


@socketio.on('SLCalc', namespace='/test')
def SLCalc(data):
	data['units_per_pip'] = 1e4
	data = dict((k,float(v)) for k,v in data.items())

	result = SL(**data)

	emit('sl_result',
		 result,
		 broadcast=False) 

@socketio.on('Order', namespace='/test')
def Order(data):

	emit('order',
		 data,
		 broadcast=False)	



@socketio.on('request_ui_data', namespace='/test')
def request_ui_data(data):
	pairs = Pairs.query.all()

	result = [{'id': pair.pair_id, 'pair': pair.pair, 'units_per_pip': float(pair.units_per_pip_usd), 'comission': float(pair.comission)} for pair in pairs]
	print(result)
	emit('ui_data',
		 json.dumps(result),
		 broadcast=False)	

@socketio.on('request_pair_price', namespace='/test')
def request_pair_price(data):
	pair = data['pair']
	api_key = app.config.get('FOREX_API')
	base_url = "https://forex.1forge.com/1.0.3/quotes?"

	url = base_url + urlencode({"pairs": pair, "api_key": api_key})	
	response = urllib.request.urlopen(url)
	price = json.loads(response.read())[0]['bid']

	emit('serve_pair_price',
		 {'price': price},
		 broadcast=False)
	

