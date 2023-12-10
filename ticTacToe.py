EMPTY = ''
O = 'O'
X = 'X'

class TicTacToeBoard:
    def __init__(self):
        self.board = [[EMPTY for _ in range(3)] for _ in range (3)]
    
    def board_state(self):
        return self.board
    
    def make_move(self, x, y, mark):
        if not self.validate_move(x, y):
            return False
        
        if mark not in [O, X]:
            return False
    
        self.board[x][y] = mark
        return True
        
    def validate_move(self, x, y):
        return self.board[x][y] == EMPTY
    
    def check_draw(self):
        for row in self.board:
            if EMPTY in row:
                return False

        return True
    
    def print_board(self):
        for row in self.board:
            print(' | '.join(row))
            print('-' * 9)
    
    # returns 0 if no winner, 1 if O wins, 2 if X wins
    def check_winner(self):
        for i, row in enumerate(self.board):
            #row 
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != EMPTY:
                return self.board[i][0]
            
            #column
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != EMPTY:
                return self.board[0][i]
            
            if self.board[0][0] == self.board[1][1] == self.board[2][2] != EMPTY:
                return self.board[0][0]
            
            if self.board[0][2] == self.board[1][1] == self.board[2][0] != EMPTY:
                return self.board[1][1]
            
        return ''             