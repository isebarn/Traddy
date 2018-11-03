from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
from app import app, socketio, db


@socketio.on('SLCalc', namespace='/test')
def test_message(data):
	print(data['price'])
	print(data['TP_price'])
	print(data['SL_price'])
	print(data['min_win_ratio'])
	print(data['max_loss'])
	print(data['money'])
