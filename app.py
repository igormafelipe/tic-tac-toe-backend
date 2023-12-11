from flask import Flask, jsonify, session
from gameManager import gameManager
from flask_cors import CORS
from flask_socketio import SocketIO
# from flask_cors import CORS
# from engineio.async_drivers import gevent

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
manager = gameManager()

# Allow CORS for all routes under /
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/', methods=["GET", "POST"])
def home():
    return "<h1>Welcome to big tic tac toe<h1>"

@app.route('/new_game')
def new_game():
    return manager.create_game()

@app.route('/get_board/<game_id>')
# will need a game id
def get_board(game_id):
    if game_id in manager.games:
        game = manager.games[game_id]
        return jsonify({'board': game.get_board()})
    else:
        # Game ID not found, returning a JSON response with an error message and status code
        return jsonify({'error': f"Game ID '{game_id}' not found"}), 404

@app.route('/check_draw')
# will need a game id
def check_draw():
    pass

@app.route('/check_winner')
# will need a game id
def check_winner():
    pass

@app.route('/make_move')
# will need a game id
def make_move():
    pass

if __name__ == '__main__':
    app.run()