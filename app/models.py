from app import db
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref



class Pairs(db.Model):
	pair_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	pair = db.Column(db.String(64), unique=True)
	std_lot_profit_per_pip = db.Column(db.Numeric(precision=4, scale=2))
	comission = db.Column(db.Numeric(precision=4, scale=2))
	etoro_id = db.Column(db.Integer)


class Orders(db.Model):
	order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	version = db.Column(db.Integer, primary_key=True)
	pair_id = db.Column(db.Integer, ForeignKey('pairs.pair_id'))
	request = relationship("Pairs", backref=backref("pairs", uselist=False))
	units = db.Column(db.Integer)
	enter = db.Column(db.DateTime, default=datetime.utcnow)
	exit = db.Column(db.DateTime)
	price = db.Column(db.Numeric(precision=8, scale=5, asdecimal=False, decimal_return_scale=None))
	PIP = db.Column(db.Numeric(precision=5, scale=2, asdecimal=False, decimal_return_scale=None))
	sl = db.Column(db.Numeric(precision=7, scale=5, asdecimal=False, decimal_return_scale=None))
	tp = db.Column(db.Numeric(precision=7, scale=5, asdecimal=False, decimal_return_scale=None))



class SchemaVersion(db.Model):
	table_name = db.Column(db.String(64), primary_key=True)
	version_number = db.Column(db.Integer)