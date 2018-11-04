from app import db
from datetime import datetime
from sqlalchemy import ForeignKey

class Pairs(db.Model):
	pair_id = db.Column(db.Integer, primary_key=True)
	pair = db.Column(db.String(64), primary_key=True)
	units_per_pip_usd = db.Column(db.Numeric(precision=7, scale=2))
	comission = db.Column(db.Numeric(precision=4, scale=2))


class Orders(db.Model):
	order_id = db.Column(db.Integer, primary_key=True)
	pair_id = db.Column(db.Integer)
	units = db.Column(db.Integer)
	enter = db.Column(db.DateTime, default=datetime.utcnow)
	exit = db.Column(db.DateTime)
	price = db.Column(db.Numeric(precision=8, scale=5, asdecimal=False, decimal_return_scale=None))
	PIP = db.Column(db.Numeric(precision=5, scale=2, asdecimal=False, decimal_return_scale=None))


class LimitHistory(db.Model):
	limit_id = db.Column(db.Integer, primary_key=True)
	order_id = db.Column(db.Integer)
	sl = db.Column(db.Numeric(precision=7, scale=5, asdecimal=False, decimal_return_scale=None))
	tp = db.Column(db.Numeric(precision=7, scale=5, asdecimal=False, decimal_return_scale=None))

