from app import sio
from .dection import read_emotions


@sio.event
def connect(sid, environ):
    print("connect ", sid)


@sio.event
def clientToServer(sid, data):
    read_emotions(sio)
    sio.emit("serverToClient", "message from the server")
    print("message ", data)


@sio.event
def disconnect(sid):
    print("disconnect ", sid)
