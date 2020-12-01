from app import sio


@sio.event
def connect(sid, environ):
    print("connect ", sid)


@sio.event
def clientToServer(sid, data):
    sio.emit("serverToClient", data)
    print("message: ", data)


@sio.event
def disconnect(sid):
    print("disconnect ", sid)
