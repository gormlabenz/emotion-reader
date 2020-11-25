import socketio
from .dection import read_emotions

sio = socketio.Server(cors_allowed_origins="http://localhost:8080")
app = socketio.WSGIApp(sio)

read_emotions()
from .events import *