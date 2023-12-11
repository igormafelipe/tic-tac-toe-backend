from flask import Flask
from gameManager import create_game, remove_game

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to big tic tac toe"

@app.route('/new_game')
def new_game():
    return create_game()

@app.route('/end_game')
def end_game(code):
    return remove_game(code)

if __name__ == '__main__':
    app.run()