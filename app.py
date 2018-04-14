import models
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
from flask_socketio import join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
        socketio.run(app)

# handles jsons from client
@socketio.on('json')
def handle_json(json):
        print('received json: ' + str(json))

# bounce recieved events to client that sent them
@socketio.on('json')
def handle_json(json):
        send(json, json=True)

# broadcasts to all clients
@socketio.on('my event')
def handle_my_custom_event(data):
        emit('my response', data, broadcast=True)

# broadcast message originated from server (not in response to client event)
def some_function():
        socketio.emit('some event', {'data': 42})





# room stuff
@socketio.on('join')
def on_join(data):
        username = data['username']
        room = data['room']
        join_room(room)
        send(username + ' has entered the room.', room=room)

@socketio.on('leave')
def on_leave(data):
        username = data['username']
        room = data['room']
        leave_room(room)
        send(username + ' has left the room.', room=room)
