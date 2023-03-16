from flask import Flask, render_template

from flask_socketio import SocketIO, send

app = Flask(__name__)

app.config['SECRET'] = "secret123";

socketio = SocketIO(app, cros_allowed_orgins="*")


@socketio.on('message')
def handle_message(message):
    print("Received Message: " + message);
    if message != "User Connected!":
        send(message, broadcast=True)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    socketio.run(app, host="localhost")
