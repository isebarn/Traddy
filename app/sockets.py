from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
from app import app, socketio, db

import json

from app.calc import SL
from app.UI import OrdersTable

from app.models import Pairs, Orders

from app.domain import Command, Query, API


@socketio.on('SLCalc', namespace='/test')
def SLCalc(data):
	pair = Query().query_pair_data(data['pair_id'])
	data['std_lot_profit_per_pip'] = float(pair.std_lot_profit_per_pip)


	data = dict((k,float(v)) for k,v in data.items())

	result = SL(**data)

	emit('sl_result',
		 result,
		 broadcast=False) 


@socketio.on('order_handle', namespace='/test')
def order_handle(data):
	Command().create_new_order(data)
	request_order_data()

@socketio.on('request_order_data', namespace='/test')
def request_order_data():			
	orders = Query().query_all_orders()

	html = OrdersTable(orders).__html__()	

	result = {'orders_table': html}

	emit('orders_data',
		 json.dumps(result),
		 broadcast=False)	


@socketio.on('request_ui_data', namespace='/test')
def request_ui_data():
	pairs = Query().query_pair_list()

	result = [{'id': pair.pair_id, 'pair': pair.pair, 'std_lot_profit_per_pip': float(pair.std_lot_profit_per_pip), 'comission': float(pair.comission)} for pair in pairs]

	emit('ui_data',
		 json.dumps(result),
		 broadcast=False)	

@socketio.on('request_pair_price', namespace='/test')
def request_pair_price(data):
	pair = data['pair']
	
	price = API().request_pair_asking_price(pair)

	emit('serve_pair_price',
		 {'price': price},
		 broadcast=False)
	

