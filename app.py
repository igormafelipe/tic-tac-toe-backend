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
    emit('on_connect', 'connected')
    
@socketio.on('disconnect')
def handle_disconnect():
    emit('on_disconnect', 'disconnected')
    
# Rooms can have at most 2 players
rooms = {}

# User can only join a room that has 1 player in it.
# If you join a room, your symbol is automatically O
@socketio.on('join_game')
def join_game(data):
    id = data.get('id')
    user_id = request.sid
    if not id:
        emit("Must specify an ID", to=user_id) 
        return
    
    if id not in rooms:
        emit("game_not_found", to=user_id)
    elif rooms[id] == 1:
        join_room(id)
        emit("game_joined", id, to=id)
    else:
        emit("unable_to_join_game", to=user_id)

# If you create a room, your symbol is automatically X        
@socketio.on('create_game')
def create_game():
    room_id = manager.create_game()
    rooms[room_id] = 1
    join_room(room_id)
    print(room_id)
    emit("game_created", room_id, to=room_id)

@socketio.on('make_move')
def update_board(data):
    x = data.get("x", None)
    y = data.get("y", None)
    board = data.get("board", None)
    player = data.get("player", "")
    game_id = data.get("game_id", "")
    
    if x == None or y == None or board == None or player == "" or game_id == "":
        emit("board_update_failed", request.sid)
        return
       
    next_board = gameManager.games[game_id].make_move(x, y, player, board)
    emit("board_updated", data, to=game_id)
    
    next_player = "O" if player == "X" else "X"
    turn_data = {"turn" : next_player, "board" : next_board}
    emit("change_turn", turn_data, to=game_id)

# End points
@app.route('/', methods=["GET", "POST"])
def home():
    return "<h1>Welcome to big tic tac toe<h1>"

if __name__ == '__main__':
    socketio.run(app, port=5000)