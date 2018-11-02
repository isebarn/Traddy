from app import db
from datetime import datetime

class Orders(db.Model):
	order_id = db.Column(db.Integer, primary_key=True)
	pair_id = db.Column(db.Integer)
	is_long = db.Column(db.Boolean)
	enter = db.Column(db.DateTime, default=datetime.utcnow)
	exit = db.Column(db.DateTime)
	enter_price = db.Column(db.Numeric(precision=5, asdecimal=False, decimal_return_scale=None))
	exit_price = db.Column(db.Numeric(precision=5, asdecimal=False, decimal_return_scale=None))
	exit_PIP = db.Column(db.Numeric(precision=2, asdecimal=False, decimal_return_scale=None))
	units = db.Column(db.Integer)
	spread = db.Column(db.Numeric(precision=2, asdecimal=False, decimal_return_scale=None))
	SL = db.Column(db.Numeric(precision=2, asdecimal=False, decimal_return_scale=None))
	TP = db.Column(db.Numeric(precision=2, asdecimal=False, decimal_return_scale=None))
	opportunity_type = db.Column(db.Integer)

