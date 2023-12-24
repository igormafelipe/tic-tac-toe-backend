from ticTacToe import TicTacToeBoard

O = 'O'
X = 'X'
EMPTY = ' '

# X always plays first
class BigTicTacToeBoard:    
    def __init__(self) -> None:
        self.boards = [TicTacToeBoard() for i in range(9)]
        self.winners = [EMPTY for i in range(9)]
    
    def make_move(self, x, y, mark, board):
        """
        Determines the next move on the board.

        Args:oar
        - board (int): Expected to be a number from 1 to 9.

        Returns:
        - int: A number between 1 and 9, indicating the board where the next move must occur.
            Returns 0 if there's a free choice, -1 if an error occurred.
        """
        FREE_MOVE = -1
        ERROR = -2
        
        if board < 0 or board > 8:
            print(f"Invalid board location. Must be between 0 and 8")
            return ERROR
        
        if mark not in [O, X]:
            print(f"Invalid mark. Either O or X")
            return ERROR
        
        if not self.boards[board].validate_move(x, y):
            print(f"Move {x, y} is not valid")
            return ERROR
        
        if self.boards[board].check_winner() != EMPTY:
            print(f"This board already has a winner")
            return ERROR
    
        self.boards[board].make_move(x, y, mark)
        self.winners[board] = self.boards[board].check_winner()
            
        nextBoard = y * 3 + x
        if self.boards[board].check_winner() != EMPTY:
            return FREE_MOVE
        
        if self.winners[nextBoard] != EMPTY:
            return FREE_MOVE
        
        return nextBoard
        
    def check_winner(self):
        for i in range(3):
            #row 
            if self.winners[i * 3 + 0] == self.winners[i * 3 + 1] == self.winners[i * 3 +2] != EMPTY:
                return self.winners[i * 3 + 0]
            
            #column
            if self.winners[0 * 3 + i] == self.winners[1 * 3 + i] == self.winners[2 * 3 + i] != EMPTY:
                return self.winners[0 * 3 + i]
            
        if self.winners[0] == self.winners[4] == self.winners[8] != EMPTY:
            return self.winners[0]
        
        if self.winners[2] == self.winners[4] == self.winners[6] != EMPTY:
            return self.winners[0]
            
        return EMPTY
    
    def check_draw(self):
        return EMPTY not in self.winners
    
    def get_board(self):
        boards = []
        for board in self.boards:
            boards.append(board.board_state())
        return boards
    
    # for now only print first 3 boards.
    def print_board(self):
        for i in range(3):
            for j in range(3):
                board_1_row_1 = self.boards[i * 3].board_state()[j]
                board_2_row_1 = self.boards[i * 3 + 1].board_state()[j]
                board_3_row_1 = self.boards[i * 3 + 2].board_state()[j]
                
                print(' | '.join(board_1_row_1) + 
                        '    ' + 
                        ' | '.join(board_2_row_1) +
                        '    ' + 
                        ' | '.join(board_3_row_1))
            print("------------------------------------")