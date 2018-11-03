from threading import Lock

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect

from app import app, socketio, db


@app.route('/')
def index():
	return render_template('index.html', async_mode=socketio.async_mode)


if __name__ == '__main__':
	socketio.run(app, debug=True)
