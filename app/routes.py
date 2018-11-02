from threading import Lock

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect

from app import app, socketio, db

from app.models import Orders


@app.route('/')
def index():
	return render_template('index.html', async_mode=socketio.async_mode)


@socketio.on('send_id', namespace='/test')
def test_message(message):
	print(message["order_id"])
	try: 
		order_id = int(message["order_id"])
		new_order = Orders(order_id=order_id)
		db.session.add(new_order)
		db.session.commit()		
		emit('response', {'data': "Sucessfully addedd " + message["order_id"]})
	except ValueError:
		emit('response', {'data': "Failed"})



if __name__ == '__main__':
	socketio.run(app, debug=True)
