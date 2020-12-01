import socketio
import eventlet
import multiprocessing as mp
from .dection import *


sio = socketio.Server(cors_allowed_origins="http://localhost:8080")
app = socketio.WSGIApp(sio)

from .events import *


def start_server():
    eventlet.wsgi.server(eventlet.listen(("", 5000)), app)


def run():
    processes = [mp.Process(target=start_server), mp.Process(target=connect_to_server)]
    [p.start() for p in processes]
    [p.join() for p in processes]
