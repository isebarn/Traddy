from threading import Lock

from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from config import Config


async_mode = None

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'secret!'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

from app import routes, models, sockets, domain, UI