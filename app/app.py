
import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins='http://localhost:8080')
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def clientToServer(sid, data):
    sio.emit('serverToClient', 'message from the server')
    print('message ', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)