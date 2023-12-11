from flask import Flask, jsonify, request
from gameManager import gameManager
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lol'

manager = gameManager()

cors = CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(cors_allowed_origins="*", async_mode='eventlet')
socketio.init_app(app)

# Socketio functions

# user_id room: Used for private communications between server and user

@socketio.on('connect')
def handle_connect():
    user_id = request.sid
    join_room(user_id)
    emit('on_connect', 'connected')
    
@socketio.on('disconnect')
def handle_disconnect():
    user_id = request.sid
    leave_room(user_id)
    emit('on_disconnect', 'disconnected')
    
# Rooms can have at most 2 players
rooms = {}

# User can only join a room that has 1 player in it.
# If you join a room, your symbol is automatically O
@socketio.on('join_room')
def join_room_(data):
    id = data["id"]
    user_id = request.sid
    if id not in rooms:
        emit("room not found", to=user_id)
    elif rooms[id] == 1:
        join_room(id)
        emit("room joined", to=user_id)
    else:
        emit("unable to join room", to=user_id)

# If you create a room, your symbol is automatically X        
@socketio.on('create_room')
def create_room():
    room_id = manager.generate_code()
    user_id = request.sid
    while room_id in rooms:
        room_id = manager.generate_code()
        
    rooms[room_id] = 1
    join_room(room_id)
    emit({room_id: room_id}, to=user_id)

# get the board once it is updated
# player can only add a symbol to a coordinate, so pass x, y, and player
@socketio.on('board_update')
def board_update(data):
    data_to_send = {"x":data["x"], "y":data["y"], "player":data["player"]}
    emit("board_updated", data_to_send)

# on the client, would do this:
# socket.on('switch_turns', function() {
# });
@socketio.on('switch_turn')
def switch_turn():
    emit('switch_turns')

# End points

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
    socketio.run(app, port=5000)