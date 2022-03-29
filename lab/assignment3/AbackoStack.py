# Classes for the Abacko Stack game implemented in assignment3.py
# Card class for condiguration card
# BStack class for bounded stack ADT implementation
# AbackoStack class for the game board
# also contains testing for these classes
# author: Megan Sorenson

class Card:
    '''
    Card class for an abacus game
    Card can reset it's configuration, show itself, and display one of it's stacks at a time
    '''

    def __init__(self, colours, depth):
        '''
        Initializes the Card class by creating a list of beads based on the inputs
        Also checks the validity of the inputs
        colours is an int representing the number of colours in the Card
        depth is an int representing the depth of the card stacks
        '''
        # check inputs
        assert isinstance(colours, int) and isinstance(
            depth, int), 'Error: number of colours and depth must be integers'
        assert colours > 0 and depth > 0, 'Error: number of colours and depth must be greater than zero'

        self.__colours = colours
        self.__depth = depth
        self.__beads = self.select_beads()

    def select_beads(self):
        '''
        Selects letters of the alphabet for the corresponding number of colours
        and for the specified depth
        Assumes a maximum number of colours being 26
        Returns a list of strings representing the colour labels for the Card
        '''
        import random

        alphabet = list('ABCDEFGHIJKLMNOPQRSTUV')
        # choose appropriate number of colour labels and multiple by depth of Card
        # the shuffle using imported function shuffle
        beads = alphabet[:self.__colours] * self.__depth
        # shuffle beads until it's not the same as the abacko boards would be
        while beads == random.shuffle(beads):
            random.shuffle(beads)

        return beads

    def reset(self):
        '''
        Reshuffles the Card's beads to get a new configuration
        Uses the select_beads() function of the Card class
        Returns None
        '''
        self.__beads = self.select_beads()

    def show(self):
        '''
        Displays the Card 
        Returns None
        '''
        # display the beads appropriately
        for i in range(self.__depth):
            print('|', end='')  # add initial boundary symbol
            for j in range(len(self.__beads)):
                added = 1
                if j % self.__depth == i:  # jumps to next column to get the correct bead
                    print(self.__beads[j], end='')
                    # add space if not last bead
                    if j < (len(self.__beads) - self.__depth):
                        print(' ', end='')
            print('|')  # add final boundary symbol

        # print bottom statement
        print('\nfrom a list ', end='')
        print(self.__beads)

    def stack(self, number):
        '''
        Gets the ordered list of elements from top to bottom in a specified stack
        number is the stack number being returned
        Returns a list representing the requested stack
        '''
        assert number > 0 and number <= self.__colours, 'Error: number must be greater than zero and no greater than {max:d}'.format(
            max=self.__colours)
        lower_index = 0 + ((number - 1) * self.__depth)
        upper_index = self.__depth * number

        return self.__beads[lower_index:upper_index]

    def replace(self, filename, n):
        '''
        Replaces the card's configuration with the info from a given file
        Assumes that the filename exists
        filename is a str representing the txt file's name
        n is an int representing the line of the filename to read
        returns None
        '''
        # check inputs
        assert isinstance(
            n, int) and n >= 0, 'Error: n must be an integer greater or equal to 0'

        file = open(filename, 'r')
        for i in range(n):
            line = file.readline()

        line = line.strip()
        self.__beads = line.split(' ')

    def __str__(self):
        '''
        Displays unofficial representation of the Card
        Returns None
        '''
        card_string = ''

        index = 0  # keep track of which beadto add to string
        card_string += '|'
        for i in range(self.__colours):
            for j in range(self.__depth):
                card_string += self.__beads[index]
                index += 1
            if i != (self.__colours - 1):
                card_string += '||'
        card_string += '|'

        return card_string


class BStack:
    '''
    Bounded Stack implementation
    implemented using python's list class
    right side of list is the top of the stack
    '''

    def __init__(self, size):
        '''
        Initializes the BStack class by creating a list representing the stack
        Also checks the validity of the inputs
        size is an int representing the maximum amount of items that can be pushed onto the stack
        '''
        # check inputs
        assert isinstance(
            size, int) and size >= 0, 'Error: size must be a positive integer'

        self.__size = size
        self.__items = []

    def push(self, item):
        '''
        Adds a new item to the top of the stack
        item is the item being pushed to the stack
        Returns None
        '''
        # check that push is a valid action considering the state of the stack
        assert not self.isFull(), 'Error: stack is full'

        self.__items.append(item)

    def pop(self):
        '''
        Removes the top item from the stack
        Returns the item
        '''
        # check that pop is a valid action considering the state of the stack
        assert not self.isEmpty(), 'Error: stack is empty'

        return self.__items.pop()

    def peek(self):
        '''
        Returns the top item from the stack
        but does not remove it
        '''
        # check that peek is a valid action considering the state of the stack
        assert not self.isEmpty(), 'Error: stack is empty'

        return self.__items[-1]

    def isEmpty(self):
        '''
        Tests whether the stack is empty
        Returns a bool of whether the stack is empty (True) or not (False)
        '''
        return len(self.__items) == 0

    def isFull(self):
        '''
        Tests whether the stack is full
        Returns a bool of whether the stack is full (True) or not (False)
        '''
        return len(self.__items) == self.__size

    def size(self):
        '''
        Returns the number of items on the stack
        Returns an int representing the number of items on the stack
        '''
        return len(self.__items)

    def items(self):
        '''
        Returns the items of the stack as a list
        '''
        return self.__items

    def reset(self):
        '''
        Empties the stack
        Returns None
        '''
        self.__items = []


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
            self.__top_row[digit + direction] = self.__top_row[digit]
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
        # get instance and configuration stack,
        # get them on the same order
        # compare if they are the same
        for i in range(self.__stacks):
            instance_stack = []
            # reverse list to check with configuration stack
            for item in self.__bounded_stacks[i].items():
                instance_stack.insert(0, item)

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
        for index in range(len(self.__top_row)):
            print(index, end=' ')

        print()

        # display top row
        for item in self.__top_row:
            print(item, end=' ')
        if card:
            print('{card:>9}'.format(card='card'))
        else:
            print()

        # display abackostack items by row
        for index in range(self.__stacks - 1, -1, -1):
            print('|', end=' ')
            for bounded_stack in self.__bounded_stacks:
                items = []
                for bead in bounded_stack.items():
                    items.append(bead)
                # fill tems with dots if not full
                while len(items) != self.__depth:
                    items.append('.')
                print(items[index], end=' ')
            print('|', end='')
            # print card row if necessary
            if card:
                row = self.get_card_row(self.__stacks - index - 1, card)
                print('    {row}'.format(row=row))
            else:
                print()

        # display bottom row
        bottom = '+' + ('-' * ((self.__stacks * 2) + 1)) + '+'
        if card:
            print('{abacko_bottom}{card_bottom:>15} moves'.format(
                abacko_bottom=bottom, card_bottom=str(self.__moves)))
        else:
            print(bottom)

    def get_card_row(self, row, card):
        '''
        Creates a single row for display of the card
        row is an int representing the row being created
        card is a Card object with the rows
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

    def get_moves(self):
        '''
        Returns how many moves have been completed
        '''
        return self.__moves


# test the AbackoStack class
if __name__ == "__main__":
    # Card Testing
    print('\nTESTING CARD CLASS')
    colours = 5
    depth = 2
    test_card = Card(colours, depth)

    print('Card display:')
    test_card.show()
    print('depth:', depth)
    print('colours:', colours)

    # test reset()
    print('\nTEST1: test reset()')
    print('test1: before reset')
    test_card.show()
    test_card.reset()
    print('test1: after reset')
    test_card.show()

    # test stack()
    print('\nTEST2: test stack()')
    print('first stack:')
    print(test_card.stack(1))
    if len(test_card.stack(1)) == depth:
        print('test2: PASSED')
    else:
        print('test2: unexpected length of stack')
        print('test2: FAILED')

    # test initializing with invalid parameters
    print('\nTEST3: test initialization of Card with invalid parameters')
    try:
        Card('a', 2)
        Card(3, -5)
    except:
        print('test3: PASSED')
    else:
        print('test3: initialized stack with invalid parameters')
        print('test3: FAILED')

    # test __str__()
    print('\nTEST3: testing unofficial string representation')
    print('test3: card using show()')
    test_card.show()
    print('test3: card using print()')
    print(test_card)

    # test replace
    print('\nTEST4: testing replace using a known file')
    print('test4: card before replace')
    test_card.show()
    test_card.replace('test_replace.txt', 1)
    print('test4: card after replace')
    test_card.show()

    # BStack Testing
    print('\nTESTING BSTACK CLASS')
    max = 3
    test_stack = BStack(max)

    # test push()
    for i in range(max):
        test_stack.push(i)
    print('\nTEST1: test pushing on full stack')
    try:
        test_stack.push(1)
    except AssertionError:
        print('test1: PASSED')
    else:
        print('test1: pushed on full stack')
        print('test1: FAILED')

    # test pop()
    for i in range(max):
        test_stack.pop()
    print('\nTEST2: testing popping on empty stack')
    try:
        test_stack.pop()
    except AssertionError:
        print('test2: PASSED')
    else:
        print('test2: popped an empty stack')
        print('test2: FAILED')

    # test peek()
    test_stack.push(2)
    print('\nTEST3: test peek()')
    if test_stack.peek() == 2:
        print('test3: PASSED')
    else:
        print('test3: peek returned unexpected value')
        print('test3: FAILED')

    test_stack.pop()
    print('\nTEST4: test peek on empty list')
    try:
        test_stack.peek()
    except AssertionError:
        print('test4: PASSED')
    else:
        print('test4: peeked on empty list')
        print('test4: FAILED')

    # test isEmpty()
    print('\nTEST5: test isEmpty() on empty list')
    if test_stack.isEmpty():
        print('test5: PASSED')
    else:
        print('test5: unexpected return on isEmpty()')
        print('test5: FAILED')

    test_stack.push(3)
    print('\nTEST6: test isEmpty() on non-empty list')
    if not test_stack.isEmpty():
        print('test6: PASSED')
    else:
        print('test6: unexpected return on isEmpty()')
        print('test6: FAILED')

    # test isFull()
    test_stack.push(4)
    test_stack.push(5)
    print('\nTEST7: test isFull() on full list')
    if test_stack.isFull():
        print('test7: PASSED')
    else:
        print('test7: unexpected return on isFull()')
        print('test7: FAILED')

    test_stack.pop()
    print('\nTEST8: test isFull() on non-full list')
    if not test_stack.isFull():
        print('test8: PASSED')
    else:
        print('test8: unexpected return on isFull()')
        print('test8: FAILED')

    # test size()
    print('\nTEST9: test size()')
    if test_stack.size() == 2:
        print('test9: PASSED')
    else:
        print('test9: uenxpected size return')
        print('test9: FAILED')

    # test reset()
    test_stack.reset()
    print('\nTEST10: test reset()')
    if test_stack.isEmpty():
        print('test10: PASSED')
    else:
        print('test10: stack did not reset')
        print('test10: FAILED')

    # test initializing with wrong parameters
    print('\nTEST11: test initialization of stack with invalid parameters')
    try:
        BStack('a')
        BStack(-1)
    except:
        print('test11: PASSED')
    else:
        print('test11: initialized stack with invalid parameters')
        print('test11: FAILED')

    # Abacko Stack Testing
    print('\nTESTING ABACKOSTACK CLASS')
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
