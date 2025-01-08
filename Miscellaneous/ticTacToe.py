import random

# Define the board as a dictionary
theBoard = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
}

# Function to print the game board
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# Function to check for a winner
def checkWinner(board):
    winning_combinations = [
        ['top-L', 'top-M', 'top-R'],  # top row
        ['mid-L', 'mid-M', 'mid-R'],  # middle row
        ['low-L', 'low-M', 'low-R'],  # bottom row
        ['top-L', 'mid-L', 'low-L'],  # left column
        ['top-M', 'mid-M', 'low-M'],  # middle column
        ['top-R', 'mid-R', 'low-R'],  # right column
        ['top-L', 'mid-M', 'low-R'],  # diagonal top-left to bottom-right
        ['top-R', 'mid-M', 'low-L']   # diagonal top-right to bottom-left
    ]

    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] and board[combination[0]] != ' ':
            return board[combination[0]]  # Return the winner ('X' or 'O')
    return None  # No winner yet

# Function to check available moves
def availableMoves(board):
    return [space for space, mark in board.items() if mark == ' ']

# Function for the AI to make a move
def aiMove(board):
    # First, try to win
    for move in availableMoves(board):
        board[move] = 'O'
        if checkWinner(board) == 'O':
            return move
        board[move] = ' '  # Undo the move

    # Then, block the opponent's winning move
    for move in availableMoves(board):
        board[move] = 'X'
        if checkWinner(board) == 'X':
            board[move] = 'O'  # Block the opponent
            return move
        board[move] = ' '  # Undo the move

    # Otherwise, pick a random available move
    return random.choice(availableMoves(board))

# Main game loop
turn = 'X'  # Player 'X' goes first
winner = None

for i in range(9):
    printBoard(theBoard)

    if turn == 'X':
        print('Player X, move on which space?')
        move = input().strip()

        if move in theBoard and theBoard[move] == ' ':
            theBoard[move] = turn
            winner = checkWinner(theBoard)
            if winner:
                printBoard(theBoard)
                print(f"Player {winner} wins!")
                break
            turn = 'O'  # Switch to AI's turn after user move
        else:
            print("Invalid move. Try again.")
            continue

    # Now, handle the AI's turn after the user has made a move
    if turn == 'O' and winner is None:  # Only if there's no winner yet
        move = aiMove(theBoard)
        print(f"AI chooses {move}")
        theBoard[move] = turn
        winner = checkWinner(theBoard)
        if winner:
            printBoard(theBoard)
            print(f"Player {winner} wins!")
            break
        turn = 'X'  # Switch back to player's turn after AI move

# If the board is full and no winner, it's a draw
if winner is None and all(space != ' ' for space in theBoard.values()):
    print("It's a draw!")
    printBoard(theBoard)
