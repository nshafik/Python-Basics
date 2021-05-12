
import random

from IPython.display import clear_output

def display_board(board):
    print('{} | {} | {}'.format( board[1],board[2],board[3]))
    print('{} | {} | {}'.format( board[4],board[5],board[6]))
    print('{} | {} | {}'.format( board[7],board[8],board[9]))

def place_marker(board, marker, position):
    board[position]=marker.upper()
    clear_output()
    display_board(board)
    
def player_input():
    while True:
        xoro=input('X or O')
        if xoro.upper() in ('X','O'):
            if xoro.upper()=='X':
                return('X','O')
            else:
                return('O','X')

def space_check(board, position):
    try:
        position=int(position)
        if position not in full:
            return space_check(board, (input('Please choose a number between 1 and 9 ')))
        elif position in Positions:
            return space_check(board, int(input('this place was already taken, choose another! ')))
        else:
            return position
    except:
        return space_check(board, (input('this is not an integer! ')))
    
def full_board_check(positions):
    return (full == sorted(positions))
 

def choose_first(a,b):
    return (random.choice([a,b]))
    

def play(player):
    position=space_check(board, (input('{} choose a position'.format(player))))
    
    place_marker(board, player, position)
    Positions.append(position)

def win_check(board, mark):
    x=( board[1]==board[2]==board[3]==mark or
       board[4]==board[5]==board[6]==mark or 
       board[7]==board[8]==board[9]==mark or
       board[1]==board[5]==board[9]==mark or
       board[3]==board[5]==board[7]==mark or
       board[1]==board[4]==board[7]==mark or
       board[2]==board[5]==board[8]==mark or
       board[3]==board[6]==board[9]==mark)
    return x

def replay():
    while True:
        x=input('DO YOU WANT TO PLAY AGAIN?')
        if x.lower()=='yes':
            clear_output()
            return True
        elif x.lower()=='no':
            clear_output()
            return False
        else: print('reply by yes or no')

print('Welcome to Tic Tac Toe!')

while True:
    board=[' ']*10
    Positions=[]
    full=[1,2,3,4,5,6,7,8,9]
    print('Player1 ')
    Player1,Player2=player_input()
    print('Player1: {} \nPlayer2:{} '.format(Player1,Player2))
    
    first=choose_first('Player1','Player2')
    print('{} will go first'.format(first))
    while True:
        if first=='Player1':
            play(Player1)

            if win_check(board,Player1.upper()):
                print('Player1 WON')
                break
                
            if full_board_check(Positions):
                print('no places left!')
                break
            else:
                play(Player2)
                if win_check(board,Player2.upper()):
                    print('Player2 WON')
                    break
                if full_board_check(Positions):
                    print('no places left!')
                    break
        else:
            play(Player2)
            if win_check(board,Player2.upper()):
                print('Player2 WON')
                break
            if full_board_check(Positions):
                print('no places left!')
                break
            else:
                play(Player1)
                if win_check(board,Player1.upper()):
                    print('Player1 WON')
                    break 
                if full_board_check(Positions):
                    print('no places left!')
                    break
                
    

        
        
        
    if not replay():
        print('Bye!')
        break
