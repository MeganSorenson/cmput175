# ----------------------------------------------------
# Lab 3: Numerical Tic Tac Toe class
#
# Author: Megan Sorenson
# ----------------------------------------------------

class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''
        self.board = []  # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board
        # which numbers are still available to input
        self.available_board_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.row_col_options = (0, 1, 2)

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
        if row in self.row_col_options and col in self.row_col_options:  # check if row and col valid
            if self.board[row][col] > 0:
                return False
            else:
                return True
        else:
            return False

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
        # check if the square is empty and the number hasn't already on the board
        if self.squareIsEmpty(row, col) and num in self.available_board_numbers:
            self.board[row][col] = num
            # make that number unavailable for future use
            self.available_board_numbers.remove(num)
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
                    # row win
                    if 0 not in self.board[row_index] and sum(self.board[row_index]) == 15:
                        return True
                    # create first diagonal list
                    diag1.append(self.board[row_index][row_index])
                    # create second diagonal list
                    diag2.append(self.board[row_index]
                                 [self.size - 1 - row_index])
            if 0 not in col and sum(col) == 15:  # column win
                return True
        if 0 not in diag1 and sum(diag1) == 15:  # diagonal win
            return True
        elif 0 not in diag2 and sum(diag2) == 15:  # diagonal win
            return True
        else:
            return False


if __name__ == "__main__":
    # TEST EACH METHOD THOROUGHLY HERE
    # suggested tests are provided as comments, but more tests may be required

    # Test 1: start by creating empty board and checking the contents of the board attribute
    myBoard = NumTicTacToe()

    print("\nTEST 1: check inital contents of board")
    print('Contents of board attribute when object first created:')
    print(myBoard.board)

    # Test 2: does the empty board display properly?
    print("\nTEST 2: check drawBoard()")
    myBoard.drawBoard()

    # Test 3: assign a number to an empty square and display
    #   first check if square is empty
    #   then add number to empty sqaure
    #   then check if square is empty
    row = 1
    col = 1
    input_value3 = 5
    print("\nTEST 3: check squareIsEmpty()")
    if myBoard.squareIsEmpty(row, col):
        print("test3: square is initially empty, now input value...")
        myBoard.update(row, col, input_value3)
        if not myBoard.squareIsEmpty(row, col):
            print("test3: square is now filled")
            print("test3: PASSED")
        else:
            print("test3: FAILED")
    else:
        print("test3: FAILED")

    # Test 4: try to assign a number to a non-empty square. What happens?
    #   try to input number into sqaure filled by Test 3
    input_value4 = 1
    print("\nTEST 4: check update() on non-empty cell")
    if not myBoard.update(row, col, input_value4):
        print("test4: board not updated")
        print("test4: PASSED")
    else:
        print("test4: FAILED")

    # Test 5: check if the board has a winner. Should there be a winner after only 1 entry?
    print("\nTEST 5: check isWinner() after one entry")
    if not myBoard.isWinner():
        print("test5: no win yet")
        print("test5: PASSED")
    else:
        print("test5: FAILED")

    # Test 6: check if the board is full. Should it be full after only 1 entry?
    print("\nTEST 6: check boardFull() after one entry")
    if not myBoard.boardFull():
        print("test6: board not full")
        print("test6: PASSED")
    else:
        print("test6: FAILED")

    # Test 7: add values to the board so that any line adds up to 15. Display
    #   check horizontal, vertical and diagonal wins
    #   use the isWinner() to check if win
    print("\nTEST 7A: check horizontal win")
    myBoard7A = NumTicTacToe()
    inputs = (2, 8, 5)
    # add values to row
    for col in range(3):
        myBoard7A.update(0, col, inputs[col])
    print("test7a: board after adding row of sum 15... check win")
    myBoard7A.drawBoard()
    # check if win
    if myBoard7A.isWinner():
        print("test7a: row win")
        print("test7a: PASSED")
    else:
        print("test7a: FAILED")

    print("\nTEST 7B: check vertical win")
    myBoard7B = NumTicTacToe()
    # add values to column
    for row in range(3):
        myBoard7B.update(row, 0, inputs[row])
    print("test7b: board after adding col of sum 15... check win")
    myBoard7B.drawBoard()
    # check if win
    if myBoard7B.isWinner():
        print("test7b: col win")
        print("test7b: PASSED")
    else:
        print("test7b: FAILED")

    print("\nTEST 7C: check diagonal win")
    myBoard7C = NumTicTacToe()
    # add values to diagonal
    for row_col in range(3):
        myBoard7C.update(row_col, row_col, inputs[row_col])
    print("test7c: board after adding diagonal of sum 15... check win")
    myBoard7C.drawBoard()
    # check if win
    if myBoard7C.isWinner():
        print("test7c: diagonal win")
        print("test7c: PASSED")
    else:
        print("test7c: FAILED")

    # Test 8: check if the board is full after filling it
    print("\nTEST 8: check boardFull() after filling board")
    input_value = 1  # will be incremented each input
    myBoard8 = NumTicTacToe()
    # check if initally full
    if not myBoard8.boardFull():
        print("test8: board initially not full... fill board")
    else:
        print("test8: FAILED")
    # fill board
    for row in range(3):
        for col in range(3):
            myBoard8.update(row, col, input_value)
            input_value += 1
    if myBoard8.boardFull():
        print("test8: board now full")
        print("test8: PASSED")
    else:
        print("test8: FAILED")

    # Test 9: check isWinner() if row sums to 15 but not full
    print("\nTEST 9: check isWinner() when row/col/diag not full")
    myBoard9 = NumTicTacToe()
    input1 = 9
    input2 = 6
    # update row with two numbers
    myBoard9.update(0, 0, input1)
    myBoard9.update(0, 1, input2)
    # display board
    myBoard9.drawBoard()
    # check win
    if not myBoard.isWinner():
        print("test9: no win")
        print("test9: PASSED")
    else:
        print("test9: FAILED")

    # Test 10: check update() if number already on board
    myBoard10 = NumTicTacToe()
    input_num = 3
    print("\nTEST 10: check update() if number already on board")
    # initally input number
    myBoard10.update(0, 0, input_num)
    # check if can input same number in diferent square
    if not myBoard10.update(1, 1, input_num):
        print("test10: board not updated")
        print("test10: PASSED")
    else:
        print("test10: FAILED")

    # Test 11: check update() if row/col not in board
    #   use same board as test 10 but number other than 3
    row = 5
    print("\nTEST 11: check update() if row/col doesn't exist")
    if not myBoard10.update(row, 0, 1):
        print("test11: board not updated")
        print("test11: PASSED")
    else:
        print("test11: FAILED")

    # Test 12: check update if num not an int
    #   use same board as test 10 but square not already used
    input_value = 'a'
    print("\nTEST 12: check update() if input value is not an integer")
    if not myBoard10.update(2, 2, input_value):
        print("test12: board not updated")
        print("test12: PASSED")
    else:
        print("test12: FAILED")

    # Test 13: check squareIsEmpty() if row/col not in board
    #   use same board as test 10
    row = 5
    print("\nTEST 13: check squareIsEmpty() if row/col doesn't exist")
    if not myBoard10.squareIsEmpty(row, 0):
        print("test13: square not empty (or does not exist)")
        print("test13: PASSED")
    else:
        print("test13: FAILED")
