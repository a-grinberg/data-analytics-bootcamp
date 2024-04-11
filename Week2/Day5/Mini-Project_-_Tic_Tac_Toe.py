# Instructions
# The game is played on a grid that’s 3 squares by 3 squares.
# Players take turns putting their marks (O or X) in empty squares.
# The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
# When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

# Hint
# To do this project, you basically need to create four functions:

# display_board() – To display the Tic Tac Toe board (GUI).
# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above.
# Note: The 4 functions above are just an example. You can implement many more helper functions or choose a completely different appoach if you want.

# Tips : Consider The Following:
# What functionality will need to accur every turn to make this program work?
# After contemplating the question above, think about splitting your code into smaller pieces (functions).
# Remember to follow the single responsibility principle! each function should do one thing and do it well!

def display_board(board):
    print('*'*17)
    for cell in board:
        print(f'*   {cell[0]} | {cell[1]} | {cell[2]}   *')
        print(f'*  ---|---|---  *')
    print('*'*17)


def player_input(player):
    print(f"Player {player}'s turn..")
    row = int(input('Enter row: '))
    column = int(input('Enter column: '))
    return (row, column)

def check_cell(cell, board):
    if board[cell[0]][cell[1]] not in 'XO':
        return True
    print('Cell is occupied! Try again!')
    return False

def check_win(board, sign):
    row = [''.join(row) for row in board]
    column = [''.join(col) for col in zip(*board)]
    diagonal = [''.join(board[0][0]+board[1][1]+board[2][2]), ''.join(board[1][2]+board[1][1]+board[2][0])]
    return sign*3 in row + column + diagonal

def play():
    board = [[' ' for row in range(3)] for column in range(3)]
    display_board(board)
    player1 = 'O'
    player2 = 'X'
    current_player = player1
    while True:
        coords = player_input(current_player)
        while check_cell(coords, board) == False:
            coords = player_input(current_player)
        board[coords[0]][coords[1]] = current_player
        display_board(board)
        if ' ' not in [i for r in board for i in r]:
            print(f'Tie!')
            break
        if check_win(board, current_player):
            print(f'Winner is {current_player}!')
            break
        current_player = player2 if current_player == player1 else player1
    if input('Wanna play again? (y/n) ') == 'y':
        play()

play()