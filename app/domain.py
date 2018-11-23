from app import app, db
from app.models import Pairs, Orders

from urllib.parse import urlencode, quote_plus
import urllib.request

import json


class Command():

	def create_new_order(self, data):
		order = Orders()
		order.pair_id = data['pair_id']
		order.price = data['price']
		order.units = data['units']
		order.tp = data['TP']
		order.sl = data['SL']
		order.version = 1
		db.session.add(order)
		db.session.commit()		

class Query():

	def query_all_orders(self):
		return db.session.query(Orders, Pairs).filter(Orders.pair_id == Pairs.pair_id).all()

	def query_pair_data(self, pair_id):
		return Pairs.query.filter_by(pair_id = pair_id).all()[0]

	def query_pair_list(self):
		return Pairs.query.all()

class API():
	API_base_url = "https://forex.1forge.com/1.0.3/quotes?"

	def request_pair_asking_price(self, pair):
		api_key = app.config.get('FOREX_API')
		base_url = self.API_base_url

		url = base_url + urlencode({"pairs": pair, "api_key": api_key})	
		response = urllib.request.urlopen(url)
		price = json.loads(response.read())[0]['bid']

		return price