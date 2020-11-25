import eventlet
from app import app

if __name__ == "__main__":
    eventlet.wsgi.server(eventlet.listen(("", 5000)), app)
