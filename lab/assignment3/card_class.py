class Card:
    '''
    Card class for an abacus game
    Card can reset it's configuration, show itself, and display one of it's stacks at a time
    '''

    def __init__(self, colours, depth):
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
