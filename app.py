'''
    Multiple controllers:
        
        
'''

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from rest_api import *
import os

app = Flask(__name__)

app.register_blueprint(api)

socketio = SocketIO(app)

@app.route("/tinfo/admin", methods = ['GET', 'POST'])
def admin():
    return render_template("index.html")

@app.route("/tinfo", methods = ['GET', 'POST'])
def index():
    return render_template("message.html")

@socketio.on('connect')
def connected():
    print('connect')

'''
@app.route("/")
def hello():
    return "Hello World!"
'''

if __name__ == "__main__":

    socketio.run(
        app, 
        debug = True
    )
    
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    
    app.run(
        host = host, 
        port = port, 
        use_reloader = False
    )


