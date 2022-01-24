# ----------------------------------------------------
# Lab 3: Numerical Tic Tac Toe class
#
# Author:
# Collaborators:
# References:
# ----------------------------------------------------

# SHOULD I BE CHECKING IF THE NUMBER FROM 1-9 IS ALREADY ON THE BOARD?


class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''
        self.board = []  # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board

        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)

    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        # TO DO: delete pass and print out formatted board
        # e.g. an empty board should look like this:
        #    0   1   2
        # 0    |   |
        #   -----------
        # 1    |   |
        #   -----------
        # 2    |   |

        print()
        print('  ', end='')
        for col_index in range(self.size):
            print('{index:^3d}'.format(index=col_index), end='')  # col index
            print(' ', end='')
        print()
        for row_index in range(self.size):
            print('{index:<2d}'.format(index=row_index), end='')  # row index
            for col_index in range(self.size):
                # check if the cell_value is empty (0)
                # if yes, make cell value a space
                # otherwise, find the appropriate int value
                if self.squareIsEmpty(row_index, col_index):
                    cell_value = ' '
                else:
                    cell_value = self.board[row_index][col_index]
                print('{value:^3}'.format(value=cell_value),
                      end='')  # cell contents
                if col_index != 2:
                    print('|', end='')
                else:
                    print()
            if row_index != 2:
                separator = '-' * 11
                print('{line:>13s}'.format(line=separator))

    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        # TO DO: delete pass and complete method
        if self.board[row][col] > 0:
            return False
        else:
            return True

    def update(self, row, col, num):
        '''
        Assigns the integer, num, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           num (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        # TO DO: delete pass and complete method
        if self.squareIsEmpty(row, col):
            self.board[row][col] = num
            return True
        else:
            return False

    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        # TO DO: delete pass and complete method
        board_full = True
        for row_index in range(self.size):
            for col_index in range(self.size):
                if self.squareIsEmpty(row_index, col_index):
                    board_full = False

        return board_full

    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        # TO DO: delete pass and complete method
        diag1 = []
        diag2 = []
        for col_index in range(self.size):
            col = []
            for row_index in range(self.size):
                # create column list
                col.append(self.board[row_index][col_index])
                if col_index == 0:  # only need to check row win and diagonal win once
                    if sum(self.board[row_index]) == 15:  # row win
                        return True
                    # create first diagonal list
                    diag1.append(self.board[row_index][row_index])
                    # create second diagonal list
                    diag2.append(self.board[row_index]
                                 [self.size - 1 - row_index])
            if sum(col) == 15:  # column win
                return True
        if sum(diag1) == 15 or sum(diag2) == 15:  # diagonal win
            return True
        else:
            return False


if __name__ == "__main__":
    # TEST EACH METHOD THOROUGHLY HERE
    # suggested tests are provided as comments, but more tests may be required

    # start by creating empty board and checking the contents of the board attribute
    myBoard = NumTicTacToe()
    print('Contents of board attribute when object first created:')
    print(myBoard.board)

    # does the empty board display properly?
    myBoard.drawBoard()

    # assign a number to an empty square and display
    num = int(input('Player, please enter a number (1-9): '))
    row = int(input('Player, please enter a row: '))
    col = int(input('Player 1, please enter a column: '))
    myBoard.update(row, col, num)
    myBoard.drawBoard()

    # try to assign a number to a non-empty square. What happens?
    #num = int(input('Player, please enter a number (1-9): '))
    #row = int(input('Player, please enter a row: '))
    #col = int(input('Player 1, please enter a column: '))
    #myBoard.update(row, col, num)
    # myBoard.drawBoard()

    # check if the board has a winner. Should there be a winner after only 1 entry?
    if myBoard.isWinner():
        print('winner')
    else:
        print('no winner yet')

    # check if the board is full. Should it be full after only 1 entry?
    if myBoard.boardFull():
        print('board full')
    else:
        print('board not full')

    # add values to the board so that any line adds up to 15. Display
    for i in range(3):
        num = int(input('Player, please enter a number (1-9): '))
        row = int(input('Player, please enter a row: '))
        col = int(input('Player 1, please enter a column: '))
        myBoard.update(row, col, num)
        myBoard.drawBoard()

    # check if the board has a winner
    if myBoard.isWinner():
        print('winner')
    else:
        print('no winner')

    # check if the board is full
    if myBoard.boardFull():
        print('board full')
    else:
        print('board not full')

    # write additional tests, as needed
    # add items unitl board full
    while not myBoard.boardFull():
        num = int(input('Player, please enter a number (1-9): '))
        row = int(input('Player, please enter a row: '))
        col = int(input('Player 1, please enter a column: '))
        myBoard.update(row, col, num)
        myBoard.drawBoard()
    # check if winner after board full
    if myBoard.isWinner():
        print('winner')
    else:
        print('no winner')
