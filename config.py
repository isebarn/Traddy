import os 

class Config(object):
	# ...
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
	FOREX_API = os.environ.get('FOREX_API')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	DEBUG=True