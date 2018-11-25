from app import app, db
from app.models import Pairs, Orders

from urllib.parse import urlencode, quote_plus
import urllib.request

import json

# TAKA TIL
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column, row, widgetbox
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn, CheckboxGroup
from bokeh.models import ColumnDataSource
from bokeh.sampledata.stocks import MSFT
import pandas as pd
from math import pi




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

	def query_pair_etoro_id(self, pair):
		return Pairs.query.filter_by(pair = pair).all()[0].etoro_id

	def query_all_orders(self):
		return db.session.query(Orders, Pairs).filter(Orders.pair_id == Pairs.pair_id).all()

	def query_pair_data(self, pair_id):
		return Pairs.query.filter_by(pair_id = pair_id).all()[0]

	def query_pair_list(self):
		return Pairs.query.all()

class API():
	API_base_url = "https://forex.1forge.com/1.0.3/quotes?"
	eToro_base_url = "https://candle.etoro.com/candles/desc.json"

	def request_pair_candle_data(self, pair, timespan='OneHour', count=50):
		url = self.eToro_base_url

		url += '/' + timespan
		url += '/' + str(count)
		url += '/' + str(pair)

		response = urllib.request.urlopen(url)
		body = json.loads(response.read())
		candles = body["Candles"][0]["Candles"]

		candle_data = [
			{'c': x['Close'],'h': x['High'],'l': x['Low'],'o':x['Open'],'t': x['FromDate']} 
			for x in candles]		

		return candle_data


	def plot_dataframe(self, df=None):
		df["date"] = pd.to_datetime(df["date"])

		inc = df.close > df.open
		dec = df.open > df.close
		w = 5*60*1000 # half day in ms

		TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

		p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title = "MSFT Candlestick")
		p.xaxis.major_label_orientation = pi/4
		p.grid.grid_line_alpha=0.3

		p.segment(df.date, df.high, df.date, df.low, color="black")
		p.vbar(df.date[inc], w, df.open[inc], df.close[inc], fill_color="#D5E1DD", line_color="black")
		p.vbar(df.date[dec], w, df.open[dec], df.close[dec], fill_color="#F2583E", line_color="black")

		return p

	def json_candle_to_pandas_df(self, json_candles):
		low = [x["Low"] for x in json_candles]
		high = [x["High"] for x in json_candles]
		open_price = [x["Open"] for x in json_candles]
		close_price = [x["Close"] for x in json_candles]
		start = [x["FromDate"] for x in json_candles]
		
		data = {'low': low, 'high': high, 'open': open_price, 'close': close_price, 'date': start}
		df = pd.DataFrame(data=data)

		return df


	def request_pair_asking_price(self, pair):
		api_key = app.config.get('FOREX_API')
		base_url = self.API_base_url

		url = base_url + urlencode({"pairs": pair, "api_key": api_key})	
		response = urllib.request.urlopen(url)
		price = json.loads(response.read())[0]['bid']

		return price

'''
a = API()
pp = a.request_pair_candle_data(1, 'OneHour', 3)
p = [{'c': x['Close'],'h': x['High'],'l': x['Low'],'o':x['Open'],'t': x['FromDate']} for x in pp]
print(p)
'''