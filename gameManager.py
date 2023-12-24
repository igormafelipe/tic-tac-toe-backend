import string
import random
from bigTicTacToe import BigTicTacToeBoard

N=7

class gameManager:
    def __init__(self):
        self.games = {}
        
    def generate_code(self):
        code = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))
        
        while code in self.games:
            code = self.generate_code()
        
        return code
        
    def create_game(self):
        code = self.generate_code()
        self.games[code] = BigTicTacToeBoard()
        
        return code
    
    def remove_game(self, code):
        if not code:
            return

        self.games[code] = None
        
    def make_move(self, game_id, x, y, player, board):
        if game_id not in self.games:
            return -2
        
        return self.games[game_id].make_move(x, y, player, board)
    
    def check_game_winner(self, game_id):
        if game_id not in self.games:
            return -2
        
        return self.games[game_id].check_winner()
    
    def check_game_draw(self, game_id):
        if game_id not in self.games:
            return -2
        
        return self.games[game_id].check_draw()