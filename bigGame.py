from bigTicTacToe import BigTicTacToeBoard
from time import sleep

def main():
    bigBoard = BigTicTacToeBoard()
    
    next_board = 0
    while True:
        for player in ['X', 'O']:
            if next_board == 0: 
                cell = input(f"{player} turn, format x,y,board: ")
                x,y,board = cell.split(',')
                next_board = board
            else:
                cell = input(f"{player} turn, format x,y: ")
                x,y = cell.split(',')
            
            next_board = bigBoard.make_move(int(x), int(y), player, int(next_board))
            while next_board == -1:
                sleep(1)
                bigBoard.print_board()
                cell = input(f"{player} turn, format x,y,board: ")
                x, y, board = cell.split(',')
                next_board = bigBoard.make_move(int(x), int(y), player, int(next_board))
            
            bigBoard.print_board()
            
            if bigBoard.check_winner() == player:
                print(f"Congratiluations {player}, you win!")
                return
            
            if bigBoard.check_draw() == True:
                print(f"It's a draw!")
                return

if __name__  == "__main__":
    main()