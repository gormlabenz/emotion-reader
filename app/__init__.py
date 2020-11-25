from multiprocessing.context import Process
import socketio
import eventlet
import multiprocessing as mp
from .dection import *
import time
from socket_io_emitter import Emitter

io = Emitter({"host": "localhost", "port": 6379})
io.Emit("broadcast event", "Hello from socket.io-python-emitter")

sio = socketio.Server(cors_allowed_origins="http://localhost:8080")
app = socketio.WSGIApp(sio)

from .events import *


def start_server():
    eventlet.wsgi.server(eventlet.listen(("", 5000)), app)


def start_recognizer():
    while True:
        sio.emit("serverToClient", "message from init", callback=print("sucess"))
        time.sleep(1)


def run():
    sio.start_background_task(start_recognizer)
    eventlet.wsgi.server(eventlet.listen(("", 5000)), app)
    """ processes = [mp.Process(target=start_server), mp.Process(target=start_recognizer)]
    [p.start() for p in processes]
    [p.join() for p in processes] """
