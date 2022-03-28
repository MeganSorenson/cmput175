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

        #alphabet = list('ABCDEFGHIJKLMNOPQRSTUV')
        # choose appropriate number of colour labels and multiple by depth of Card
        # the shuffle using imported function shuffle
        #beads = alphabet[:self.__colours] * self.__depth
        # random.shuffle(beads)
        beads = ['B', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'C']

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


# testing the Card Class
if __name__ == "__main__":
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
