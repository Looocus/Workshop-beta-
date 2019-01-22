#-*- coding : utf-8 -*-
import os
from app import create_app, db, socketio
from app.models import User, Role, Message
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


app = create_app('development')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Message=Message)


#manager.add_command("shell", Shell(make_context=make_shell_context()))
manager.add_command('db', MigrateCommand)
#smanager.add_command('run',socketio.run(app=app, host="0.0.0.0", port=5000))

if __name__ == '__main__':
    socketio.run(app=app, host='0.0.0.0', port=5000)
