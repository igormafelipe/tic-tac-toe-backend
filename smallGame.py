from ticTacToe import TicTacToeBoard
from time import sleep

def main():
    board = TicTacToeBoard()
    
    while True:
        for player in ['X', 'O']:
            cell = input(f"{player} turn, format x,y: ")
            x, y = cell.split(',')
            
            while board.make_move(int(x), int(y), player) != True:
                print("Invalid move")
                sleep(1)
                board.print_board()
                cell = input(f"{player} turn, format x,y: ")
                x, y = cell.split(',')
            
            board.print_board()
            
            if board.check_winner() == player:
                print(f"Congratiluations {player}, you win!")
                return
            
            if board.check_draw() == True:
                print(f"It's a draw!")
                return

if __name__  == "__main__":
    main()