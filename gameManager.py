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
            
        