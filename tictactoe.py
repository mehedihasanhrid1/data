import random
from colorama import init, Fore, Style

init(autoreset=True)

def display_board(board):
    def c(v):
        if v == 'X':
            return Fore.RED + v
        if v == 'O':
            return Fore.BLUE + v
        return Fore.YELLOW + v

    print()
    print(f" {c(board[0])} | {c(board[1])} | {c(board[2])}")
    print(Fore.CYAN + "-----------")
    print(f" {c(board[3])} | {c(board[4])} | {c(board[5])}")
    print(Fore.CYAN + "-----------")
    print(f" {c(board[6])} | {c(board[7])} | {c(board[8])}")
    print()

def check_win(board, s):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(board[a] == board[b] == board[c] == s for a,b,c in wins)

def check_full(board):
    return all(not x.isdigit() for x in board)

def ai_move(board, ai, player):
    for i in range(9):
        if board[i].isdigit():
            temp = board.copy()
            temp[i] = ai
            if check_win(temp, ai):
                board[i] = ai
                return

    for i in range(9):
        if board[i].isdigit():
            temp = board.copy()
            temp[i] = player
            if check_win(temp, player):
                board[i] = ai
                return
            
    board[random.choice([i for i in range(9) if board[i].isdigit()])] = ai
