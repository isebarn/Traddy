from app import db
from app.models import Pairs, Orders

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

