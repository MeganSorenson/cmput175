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


# testing the BStack Class
if __name__ == "__main__":
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
