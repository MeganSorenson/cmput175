from bounded_stack import BStack


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
        self.__top_row = [None] * (self.__stacks + 2)
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


# test the AbackoStack class
if __name__ == "__main__":
    abacko = AbackoStack(3, 4)
    abacko.moveBead('1d')
