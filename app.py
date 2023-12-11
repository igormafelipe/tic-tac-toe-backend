from flask import Flask, jsonify
from gameManager import gameManager

app = Flask(__name__)
manager = gameManager()

@app.route('/')
def home():
    return "Welcome to big tic tac toe"

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