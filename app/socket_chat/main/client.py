#-*- coding : utf-8 -*-
from flask import Flask, render_template
from flask_socketio import SocketIO,emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('socket_html')

@socketio.on('imessage', namespace='/test_conn')
def test_message(message):
    emit('message',#后端广播信息的事件名最好跟前端发送信息的事件名不一样
         {'data': message['data']},
         broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True, port=5000)
