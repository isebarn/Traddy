from flask_table import Table, Col

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