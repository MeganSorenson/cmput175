from bounded_stack import BStack
from card_class import Card


class AbackoStack:
    '''
    AbackoStack class representing the abacko stack structure
    uses bounded stacks and a list to represent the abacko game board
    '''

    def __init__(self, stacks, depth):
        '''
        Initializes an AbackoStack
        Also checks the validity of the inputs
        stacks is an int representing the number of bounded stacks on the game board
        depth in an int rep the shared depth of the stacks
        '''
        # check inputs
        assert isinstance(
            stacks, int) and stacks > 0, 'Error: number of stacks must be an integer greater than zero'
        assert isinstance(
            depth, int) and depth > 0, 'Error: depth of stacks must be an integer greater than zero'

        self.__stacks = stacks
        self.__depth = depth
        self.__bounded_stacks = self.create_stack_list()
        self.__top_row = ['.'] * (self.__stacks + 2)
        self.__moves = 0

    def create_stack_list(self):
        '''
        Creates a list of bounded stacks from the BStack class
        Returns a list of BStack objects
        '''
        stack_list = []

        # create empty stacks
        for i in range(self.__stacks):
            stack_list.append(BStack(self.__depth))
        # fill stacks with a color
        self.fill_stacks(stack_list)

        return stack_list

    def fill_stacks(self, stack_list):
        '''
        Fills stacks from a list of stacks with a color (symbolized by a letter)
        Assumes that the maximum number of colours is 26
        stack_list is a list of BStacks
        Returns None
        '''
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        index = 0  # keeps track of which letter of the alphabet to use
        for bounded_stack in stack_list:
            while not bounded_stack.isFull():
                bounded_stack.push(alphabet[index])
            index += 1

    def moveBead(self, move):
        '''
        Moves a specified bead in a specified direction based on the input
        Also checks if the move is valid
        move is a string of two characters, the first being a digit and the second being a character
        Returns None
        '''

        valid_moves = self.get_valid_moves()

        # check inputs
        assert move in valid_moves, 'Error: move must be within the following options: {valid_moves}'.format(
            valid_moves=valid_moves)

        digit = int(move[0])
        character = move[1]

        # if moving bead up
        if character == 'u':
            self.move_bead_up(digit)
        # if moving down
        elif character == 'd':
            self.move_bead_down(digit)
        # if moving left or right
        # won;t have issues here with moving left at index 0 or right at last index
        # because this is handled in the initial assert statement at the beginning of this function
        elif character in 'lr':
            self.move_bead_left_right(character, digit)

    def get_valid_moves(self):
        '''
        Finds what moves are valid given the AbackoStack
        Returns a list of strings representing valid moves
        '''
        valid_moves = []

        stack_moves = 'ud'
        top_row_moves = 'lr'
        for stack in range(1, (self.__stacks + 1)):
            for move in stack_moves:
                valid_moves.append(str(stack) + move)
        for index in range(self.__stacks + 2):
            if index == 0:  # can only move right if beginning index
                valid_moves.append(str(index) + top_row_moves[1])
            elif index == (self.__stacks + 1):  # can only move left if end index
                valid_moves.append(str(index) + top_row_moves[0])
            else:
                for move in top_row_moves:
                    valid_moves.append(str(index) + move)

        return valid_moves

    def move_bead_up(self, digit):
        '''
        Moves a bead up from a stack
        Also checks if move is valid
        digit is the stack that the bead is moving up from
        returns None
        '''
        moving_stack = self.__bounded_stacks[digit - 1]
        # check that the spot to move the bead is empty in the top row
        # if empty, remove bead from stack and add to top row
        # if not empty, raise and Exception
        if self.__top_row[digit] == '.' and not moving_stack.isEmpty():
            self.__top_row[digit] = moving_stack.pop()
            self.__moves += 1
        else:
            raise Exception(
                'Error: invalid move')

    def move_bead_down(self, digit):
        '''
        Moves a bead down from the top row
        Also checks if move is valid
        digit is the position in the top row that the bead is moving down from
        returns None
        '''
        moving_stack = self.__bounded_stacks[digit - 1]
        # check that stack to move bead to is not full
        # if not full, remove bead from top row and add to stack
        # if full, raise and Exception
        if not moving_stack.isFull() and self.__top_row[digit] != '.':
            bead = self.__top_row[digit]
            moving_stack.push(bead)
            self.__top_row[digit] = '.'
            self.__moves += 1
        else:
            raise Exception(
                'Error: invalid move')

    def move_bead_left_right(self, character, digit):
        '''
        Moves a bead left or right in the top row
        Also checks if move is valid
        character is the direction of the move
        digit is the position in the top row that the bead is moving from
        returns None
        '''
        if character == 'l':
            direction = -1
        else:
            direction = 1
        # check that spot on top row is empty
        # if empty, move bead
        # if not empty, raise Exception
        if self.__top_row[digit + direction] == '.' and self.__top_row[digit] != '.':
            bead = self.__top_row[digit]
            self.__top_row[digit + direction] = bead
            self.__top_row[digit] = '.'
            self.__moves += 1
        else:
            raise Exception(
                'Error, invalid move')

    def isSolved(self, card):
        '''
        Check if the state of the instance matches the configuration of the card
        Also checks the validity of the parameters
        card is a Card object representing the configuration being compared 
        returns a boolean... True if the configurations match, False otherwise
        '''
        # check inputs
        assert isinstance(
            card, Card), 'Error: card must be an instance of the Card class'

        match = True
        for i in range(self.__stacks):
            # these will both be lists
            instance_stack = self.__bounded_stacks[i].items()
            configuration_stack = card.stack(i + 1)
            if instance_stack != configuration_stack:  # check if they are the same
                match = False

        return match

    def reset(self):
        '''
        Resets the moves and stacks to their initial positions
        Returns None
        '''
        self.__moves = 0
        self.__bounded_stacks = self.create_stack_list()
        self.__top_row = ['.'] * (self.__stacks + 2)

    def show(self, card=None):
        '''
        Shows the state of the AbackoStack and optionally the card configuration
        card is an optional parameter of type Card
        Returns None
        '''

        # display indexes at top
        indexes = []
        for i in range(len(self.__top_row)):
            indexes.append(i)
        print(self.get_display_row(indexes))

        # display top row
        if card:
            print('{abacko_top}{card_top:>10}'.format(
                abacko_top=self.get_display_row(self.__top_row), card_top='card'))
        else:
            print(self.get_display_row(self.__top_row))

        # display abackostack items by row
        for i in range(self.__depth):
            row_items = ['|']
            for bounded_stack in self.__bounded_stacks:
                # get stack items
                stack_items = self.get_stack_items(bounded_stack)
                # add appropriate stack item to row
                row_items.append(stack_items[i])
            row_items.append('|')
            if card:
                # get card row elements and join them
                card_row = self.get_card_row(i)
                print('{abacko_row}    {card_row}'.format(
                    abacko_row=self.get_display_row(row_items), card_row=card_row))

            else:
                print(self.get_display_row(row_items))

        # display bottom row
        bottom = '+' + ('-' * ((self.__stacks * 2) + 1)) + '+'
        if card:
            print('{abacko_bottom}{card_bottom:>15} moves'.format(
                abacko_bottom=bottom, card_bottom=str(self.__moves)))
        else:
            print(bottom)

    def get_display_row(self, source):
        '''
        Creates a single row for display of the AbackoStack
        source is a list representing the source of the info for the row
        Returns a str representing the row ready for display
        '''
        row = ''
        for i in range(self.__stacks + 2):
            row += str(source[i])
            if i != (self.__stacks + 1):
                row += ' '

        return row

    def get_stack_items(self, bounded_stack):
        '''
        Gathers the items from a stack into a list and fills gaps with dots
        bounded_stack is the BStack being gathered
        Returns a list of the stack's items
        '''
        stack_items = []
        for item in bounded_stack.items():
            stack_items.append(item)
        # fill empty spots in stack_items with dots
        while len(stack_items) != self.__depth:
            stack_items.insert(0, '.')

        return stack_items

    def get_card_row(self, row):
        '''
        Creates a single row for display of the card
        row is an int representing the row being created
        returns a string representing the card row ready for display
        '''
        # gather all stacks
        card_stacks = []
        for i in range(self.__stacks):
            card_stacks.append(card.stack(i + 1))
        # create card row string using the right element from each card stack
        card_row = '|'
        for i in range(len(card_stacks)):
            card_row += card_stacks[i][row]
            if i != (len(card_stacks) - 1):  # add space if not last element
                card_row += ' '
        card_row += '|'

        return card_row


# test the AbackoStack class
if __name__ == "__main__":
    abacko = AbackoStack(3, 3)
    card = Card(3, 3)

    abacko.show()
    print()
    abacko.show(card)

    # test moveBead
    print('\nTEST1: test moveBead() with up move in empty spot')
    try:
        abacko.moveBead('2u')
    except:
        print('test1: bead not properly moved and exception raised')
        print('test1: FAILED')
    else:
        abacko.show()
        print('test1: PASSED')

    print('\nTEST2: test moveBead() with up move in non-empty spot')
    try:
        abacko.moveBead('2u')
    except:
        print('test2: PASSED')
    else:
        print('test2: bead moved into non-empty spot')
        print('test2: FAILED')

    print('\nTEST3: test moveBead() with down move in empty spot')
    try:
        abacko.moveBead('2d')
    except:
        print('test3: bead not properly moved and exception raised')
        print('test3: FAILED')
    else:
        abacko.show()
        print('test3: PASSED')

    print('\nTEST4: test moveBead() with down move in non-empty spot')
    try:
        abacko.moveBead('1d')
    except:
        print('test4: PASSED')
    else:
        print('test4: bead moved into non-empty spot')
        print('test4: FAILED')

    print('\nTEST5: test moveBead() with left move in empty spot')
    abacko.moveBead('1u')
    try:
        abacko.moveBead('1l')
    except:
        print('test5: bead not properly moved and exception raised')
        print('test5: FAILED')
    else:
        abacko.show()
        print('test5: PASSED')

    print('\nTEST6: test moveBead() with left move in non-empty spot')
    abacko.moveBead('1u')
    try:
        abacko.moveBead('1l')
    except:
        print('test6: PASSED')
    else:
        print('test6: bead moved into non-empty spot')
        print('test6: FAILED')

    print('\nTEST7: test moveBead() with right move in empty spot')
    try:
        abacko.moveBead('1r')
    except:
        print('test7: bead not properly moved and exception raised')
        print('test7: FAILED')
    else:
        abacko.show()
        print('test7: PASSED')

    print('\nTEST8: test moveBead() with right move in non-empty spot')
    abacko.moveBead('0r')
    try:
        abacko.moveBead('1r')
    except:
        print('test8: PASSED')
    else:
        print('test8: bead moved into non-empty spot')
        print('test8: FAILED')

    # test isSolved
    card = Card(3, 3)
    print('\nTEST9: test isSolved on unsolved abacko')
    if abacko.isSolved(card):
        print('test9: un-solved abacko returned as solved')
        print('test9: FAILED')
    else:
        abacko.show(card)
        print('test9: PASSED')

    # test reset
    print('\nTEST10: test reset()')
    print('test10: abacko before reset')
    abacko.show()
    print('test10: abacko after reset')
    abacko.reset()
    abacko.show()
