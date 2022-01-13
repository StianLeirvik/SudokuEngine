Board = [
    [0, 6, 0, 0, 0, 0],
    [0, 0, 0, 6, 2, 4],
    [3, 0, 4, 0, 1, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 0, 4, 5, 0],
    [0, 0, 1, 0, 0, 2]
]

# Recursively calls until board is filled
def sudokuSolver(board):
    # Printing board at every loop to see every step
    # print(Board)
    # Base-case, checks to see if there are any empty spaces to fill, if there is, then the code will recursively run
    # until there are no spaces left, if not, the board is complete.
    # Retrieves a 0 value from the board
    if not emptySpace(board):
        return True
    # Takes the indexes from the emptySpace function and gives them variable names for each index.
    else:
        row, column = emptySpace(board)

    # Loops through numbers 1-6 to check if they are valid in given square. If not, it will backtrack.
    for i in range(1,7):
        if checkValidPosition(board, i, (row, column)):
            # Testing a number in a empty spot
            board[row][column] = i

            # Recursive part of function, will call itself until base-case is met
            # Will continue building on the number from board[row][column] = i
            if sudokuSolver(board):
                return True
            # Backtrack measure, reverts the contradicting number to 0 to restart loop
            # If board[row][column] = i turns out to be a contradiction,
            # this will reset the previous 0 to a new number and restart from there
            board[row][column] = 0
    # Returns false if the number is a contradiction so that the program can continue looping
    return False

# Checks if a position is valid for a number i
def checkValidPosition(board, number, position):
    # Checks if the number is equal to any other number already in the row.
    for i in range(len(board[0])):
        # and function is there so input number is ignored because its always going to be equal to itself
        if board[position[0]][i] == number and position[1] != i:
            # Returns false if it finds a condradiction
            return False

    # Checks if the number is equal to any other number already in the column
    for i in range(len(board)):
        # and function is there so it ignores the input number
        if board[i][position[1]] == number and position[0] != i:
            # Returns false if it finds a condradiction
            return False

    # X Y variables to create boundaries for sudoku squares.
    squareX = position[1] // 2
    squareY = position[0] // 3


    # Checks if the number is equal to any other number already in the square
    # Multiplying the variables to reach the next square indexes, i.e [0,3], [5,5] or [2,0]
    for i in range(squareY * 3, squareY * 3 + 3):
        for j in range(squareX * 2, squareX * 2 + 2):
            if board[i][j] == number and (i, j) != position:
                # Returns false if it finds a condradiction
                return False
    # Returns True if there are no contradictions after all three checks
    return True

# Checks for spaces with value 0
def emptySpace(board):
    # Loops through rows and columns to find a 0's then returns its position
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                # Returns indexes of position of first 0 found
                return (i, j)
    return False

# Printing function to get a better visual of the board.
def printSudoku(board):
    # Divides the columns into segments of 3
    for i in range(len(board)):
        if i % 2 == 0 and i != 0:
            print("--------------")

        # Divides the rows into segments of 2
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            # Breakes line to properly divide the lists max index of j
            if j == 5:
                print(board[i][j])

            # Prints board into Sudoku-like pattern
            else:
                print(str(board[i][j]) + " ", end="")


printSudoku(Board)
print("/") # Divides the two boards for a simpler visual
sudokuSolver(Board)
printSudoku(Board)
