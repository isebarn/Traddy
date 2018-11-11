from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
from app import app, socketio, db

import json

from app.calc import SL

from app.models import Pairs, Orders

from urllib.parse import urlencode, quote_plus
import urllib.request

from flask_table import Table, Col


@socketio.on('SLCalc', namespace='/test')
def SLCalc(data):
	data['units_per_pip'] = 1e4
	data = dict((k,float(v)) for k,v in data.items())

	result = SL(**data)

	emit('sl_result',
		 result,
		 broadcast=False) 

@socketio.on('Order', namespace='/test')
def order_handle(data):
	order = Orders()
	order.pair_id = data['pair_id']
	order.price = data['price']
	order.units = data['units']
	order.tp = data['TP']
	order.sl = data['SL']
	order.version = 1
	db.session.add(order)
	db.session.commit()

	orders = db.session.query(Orders, Pairs).filter(Orders.pair_id == Pairs.pair_id).all()

	html = OrdersTable(orders).__html__()	

	result = {'orders': html}
	emit('orders_data',
		 json.dumps(result),
		 broadcast=False)	

# Define a table, then pass in the database records
class OrdersTable(Table):
	pair = Col('pair')
	units = Col('units')
	enter = Col('enter time')
	price = Col('price')
	sl = Col('stop loss')
	tp = Col('take profit')

	def create_item(self, order, pair):
		return {
		'pair': pair.pair,
		'units': order.units,
		'enter': order.enter,
		'price': order.price,
		'sl': order.sl,
		'tp': order.tp,
		}
		

	def __init__(self, data):
		self.items = [self.create_item(entry[0], entry[1]) for entry in data]


@socketio.on('request_order_data', namespace='/test')
def request_order_data(data):			
	orders = db.session.query(Orders, Pairs).filter(Orders.pair_id == Pairs.pair_id).all()

	html = OrdersTable(orders).__html__()	

	result = {'orders': html}
	emit('orders_data',
		 json.dumps(result),
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
	

