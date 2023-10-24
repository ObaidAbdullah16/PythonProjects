print('\n'*12)

print('Welcome to my first Python Milestone Project : \n This is a Tic Tac Toe Game')


def creating_board(board):  #1 --------------------------------------------------------------
    
    print('\n'*100)
    print(f' {board[7]}   | {board[8]}  | {board[9]} ')
    print(' ____|____|____')
    print('     |    |    ')
    print(f' {board[4]}   | {board[5]}  | {board[6]} ')
    print(' ____|____|____')
    print('     |    |    ')
    print(f' {board[1]}   | {board[2]}  | {board[3]} ')
    print('\n'*10)
    

def Player1_pick():  #2 --------------------------------------------------------------------
    
    x = 'wrong'
    options = ['X', 'O']

    while x not in options :
        
        x = input('Select your Symbol for the game (Player_1) : (X/O)')
        if x not in options:
            print("Please select only from X and O !!!")

    return x


def row_key1():  #3 -------------------------------------------------------------------------

    position = ['1','2','3','4','5','6','7','8','9'] 
    input_position = 'wrong'
    
    while input_position not in position:
        input_position = input('Enter position- player1 : ')
        if input_position not in position:
            print('Please choose a correct position !!!')

    return int(input_position)


def row_key2():  #4 -------------------------------------------------------------------------

    position = ['1','2','3','4','5','6','7','8','9'] 
    input_position = 'wrong'
    
    while input_position not in position:
        input_position = input('Enter position- player2 : ')
        if input_position not in position:
            print('Please choose a correct position !!!')

    return int(input_position)


def game_on_choice():  #5 -------------------------------------------------------------------
    
    choice = 'wrong'
    lis = ['Y','N']
    
    while choice not in lis:
        choice = input("Want to keep playing? (Y/N) : ")
        if choice not in lis:
            print("sorry, Please reply in (Y/N) !!!")
            
    if choice == 'Y':
        print('lets get started again !!')
        return True
    else:
        print('Thanks for playing !!!')
        return False
    

def game_draw(board):  #6 ------------------------------------------------------------------------
    
    draw = False
    x = 0
    for i in board:
        if i == 'X' or i == 'O':
            x += 1 
        else:
            pass
        
    if x == 9 :
        draw = True
    else:
        pass
    
    return draw


def game_win1(board):  #7------------------------------------------------------------------------

    win = False
    if board[1] == board[2] == board[3] == 'X' or board[1] == board[4] == board[7] == 'X':
        win = True
    elif board[4] == board[5] == board[6] == 'X' or board[2] == board[5] == board[8] == 'X':
        win = True
    elif board[7] == board[8] == board[9] == 'X' or board[3] == board[6] == board[9] == 'X':
        win = True
    elif board[7] == board[5] == board[3] == 'X' or board[9] == board[5] == board[1] == 'X':
        win = True
    else:
        win = False

    return win


def game_win2(board):  #8------------------------------------------------------------------------

    win = False
    if board[1] == board[2] == board[3] == 'O' or board[1] == board[4] == board[7] == 'O':
        win = True
    elif board[4] == board[5] == board[6] == 'O' or board[2] == board[5] == board[8] == 'O':
        win = True
    elif board[7] == board[8] == board[9] == 'O' or board[3] == board[6] == board[9] == 'O':
        win = True
    elif board[7] == board[5] == board[3] == 'O' or board[9] == board[5] == board[1] == 'O':
        win = True
    else:
        win = False

    return win
        

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#----------------------------------------MAIN-------------------------------------------------


next_game = True
while next_game:
    
    game_on = True
    next_game = True
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    creating_board(board)
    player1 = Player1_pick()

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'


    while game_on:
    
        creating_board(board)
        player_input = row_key1()
        board[player_input] = player1
        creating_board(board)
        
        win1 = game_win1(board)
        win2 = game_win2(board)
        draw = game_draw(board)
        
        if draw == True:
            print('sorry the match has drawn...')
            game_on = False
            break
        elif win1 == True:
            print("congratulations!! Player with 'X' has won the match")
            game_on = False
            break
        elif win2 == True:
            print("congratulations!! Player with 'O' has won the match")
            game_on = False
            break
        
        
        player_input = row_key2()
        board[player_input] = player2
        creating_board(board)


        win1 = game_win1(board)
        win2 = game_win2(board)
        draw = game_draw(board)
        
        if draw == True:
            print('sorry the match has drawn...')
            game_on = False
            break
        elif win1 == True:
            print("congratulations!! Player with 'X' has won the match")
            game_on = False
            break
        elif win2 == True:
            print("congratulations!! Player with 'O' has won the match")
            game_on = False
            break

    next_game = game_on_choice()

    if next_game == True:
        game_on = True
    else:
        game_on = False
        break


    # TOTAL 8 FUCTIONS CREATED...
    
    

    
    

    
    


    



    
    








    
