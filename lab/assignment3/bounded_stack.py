class BStack:
    '''
    Bounded Stack implementation
    implemented using python's list class
    right side of list is the top of the stack
    '''

    def __init(self, size):
        '''
        Initializes the BStack class by creating a list representing the stack
        Also checks the validity of the inputs
        size is an int representing the maximum amount of items that can be pushed onto the stack
        '''
        # check inputs
        assert size >= 0 and isinstance(
            size, int), 'Error: size must be a positive integer'

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

    def reset(self):
        '''
        Empties the stack
        Returns None
        '''
        self.__items = []
