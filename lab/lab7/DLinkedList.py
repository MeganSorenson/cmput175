# Doubly Linked List Node and List ADT implementation
# author: CMPUT 175
# modified by: Megan Sorenson

class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self, initData, initNext, initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious

        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setNext(self, newNext):
        self.next = newNext

    def setPrevious(self, newPrevious):
        self.previous = newPrevious


class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
            index = -1
        return index

    def add(self, item):
        '''
        Adds a new node to the head of the list
        item is the reference to the new node's data
        returns None
        '''
        # create new node
        # don't need to check if current is None or set current's previous to the new node
        # because the DLinkedListNode handles it in its implmentation
        new_node = DLinkedListNode(item, self.__head, None)
        # adjust head and tail of list
        self.__head = new_node
        if self.__size == 0:
            self.__tail = new_node
        # increment size of list
        self.__size += 1

    def remove(self, item):
        '''
        Removes the first element in the list that is equal to the item
        if the itme is not in the ist, it is not changed (but no exception is raised)
        item is the reference to the data of the node to be removed from the list
        returns None
        '''
        current = self.__head
        removed = False
        index = 0
        # if you haven't traversed the entire list and haven't removed a node
        while current != None and not removed:
            # if data matches, remove the node using existing methods in the class
            # don't need to increment size of list becasue pop1() and pop() handle it
            if current.getData() == item:
                # if it's the end of the list, use pop1()
                if current.getNext() == None:
                    self.pop1()
                # otherwise, use pop()
                else:
                    self.pop(index)
                removed = True
            # if the data does not match, traverse the list by one more node
            else:
                current = current.getNext()
                index += 1

    def append(self, item):
        '''
        Adds a new node to the tail of the list
        item is a reference to the data of the new node
        returns None
        '''
        # don't need to adjust the tail's next because the DLinkedListNode class already handles that in it's implmentation
        new_node = DLinkedListNode(item, None, self.__tail)
        # adjust the head and tail of the list
        self.__tail = new_node
        if self.__size == 0:
            self.__head = new_node
        # increment the size of the list
        self.__size += 1

    def insert(self, pos, item):
        '''
        Adds a new node at the given positon in the list
        pos is the the position in the list to insert the new node
        item is a refernce to the data of the new node
        returns None
        '''
        # check that pos is an int and not negative
        assert pos >= 0 and isinstance(
            pos, int), "Error: position must be a positive integer"
        # check that pos is within the length of the list
        assert pos < self.__size, "Error: position must be within the length of the list"
        # if position is 0 or size is 0, use add()
        if pos == 0 or self.__size == 0:
            self.add(item)
        # if position is end of list, use append()
        elif pos == (self.__size - 1):
            self.append(item)
        # otherwise, adjust the pointers of two existing nodes to insert the new node
        # only place where size of the list needs to be incremented
        else:
            # get next and previous node
            current = self.__head
            for i in range(pos - 1):
                current = current.getNext()
            previous_node = current
            next_node = previous_node.getNext()
            # create new node
            # don't need to adjust previous and next node because DLinkedListNode already handles it in its implementation
            DLinkedListNode(item, next_node, previous_node)
            self.__size += 1

    def pop1(self):
        '''
        Removes and returns the last item in the list
        returns the last item (before removing) in the list
        '''
        # make sure that list isn't empty
        assert self.__size > 0, "Error: list is empty"
        # get last and second last node in list
        last_node = self.__tail
        if self.__size > 1:
            penultimate_node = last_node.getPrevious()
            # change the reference to the next node of the penultimate node and adjust tail of list
            penultimate_node.setNext(None)
            self.__tail = penultimate_node
        else:
            self.__head = None
            self.__tail = None
        # increment size of list
        self.__size -= 1

        return last_node.getData()

    def pop(self, pos=None):
        '''
        Removes the item in the given position
        Exception is raised if position is outside of list
        pos is the position of the item to be removed
        returns the removed item from the list
        '''
        # Hint - incorporate pop1 when no pos argument is given
        if pos != None:
            # check that pos is an int and not negative
            assert pos >= 0 or isinstance(
                pos, int), "Error: position must be a positive integer"
            # check that pos is within the length of the list
            assert pos < self.__size, "Error: position must be within the length of the list"
        # if pos is the end of the list or no pos is given, use pos1()
        if pos == (self.__size - 1) or pos == None:
            removed_item = self.pop1()
            return removed_item
        # otherwise, adjust the pointers of the two existing nodes to remove the node
        # only place that self.__size needs to be adjusted
        else:
            current = self.__head
            for i in range(pos):
                current = current.getNext()
            removed_item = current
            # get previous and next nodes to removed item and adjust their references to next and previous
            previous_node = removed_item.getPrevious()
            next_node = removed_item.getNext()
            previous_node.setNext(next_node)
            next_node.setPrevious(previous_node)
            # increment size of list
            self.__size -= 1
            return removed_item.getData()

    def searchLarger(self, item):
        '''
        Returns the position of the first element that is larger than item
        Returns -1 if there is no item
        item is a reference to the data used for the search
        '''
        current = self.__head
        index = 0
        while current != None:
            if current.getData() > item:
                return index
            else:
                current = current.getNext()
                index += 1
        # only runs if an item is not found
        index = -1
        return index

    def getSize(self):
        '''
        Returns the number of elements in the list
        '''
        return self.__size

    def getItem(self, pos):
        '''
        Returns the item at the given position
        Exception raised if the position is outside of the list
        pos is the position of the item retrieved
        '''
        assert isinstance(pos, int), "Error: position must be an integer"
        # check that pos is within the length of the list
        assert pos < self.__size, "Error: position must be within the length of the list"
        # if position is 0, return head
        if pos == 0:
            return self.__head.getData()
        # if position is end of list, return tail
        elif pos == (self.__size - 1) or pos == -1:
            return self.__tail.getData()
        # if position is positive, traverse from head to tail to find item
        elif pos > 0:
            current = self.__head
            # get the item at the given position
            for i in range(pos):
                current = current.getNext()
            return current.getData()
        # if position is negative, traverse from tail to head to find item
        else:
            current = self.__tail
            # adjusting position to follow python's indexing
            # where -1 is the last item in the list, -2 is the second last item in the list...
            pos = (pos * -1) - 1
            # get the item at the given position
            for i in range(pos):
                current = current.getPrevious()
            return current.getData()

    def __str__(self):
        '''
        Returns a string of the elements in the doubly linked list
        with one space in between each element
        '''
        current = self.__head
        list_string = ''
        while current != None:
            # add element to list string
            list_string += str(current.getData())
            # if it isn;t the last element, add a space before the nexte element
            if current.getNext() != None:
                list_string += ' '
            current = current.getNext()
        return list_string


def test():

    linked_list = DLinkedList()

    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    linked_list.add("World")
    linked_list.add("Hello")

    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(0) ==
               "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    int_list2 = DLinkedList()

    for i in range(0, 10):
        int_list2.add(i)
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"

    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"

    for i in range(21, 23):
        int_list2.insert(0, i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"

    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"

    int_list = DLinkedList()

    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    for i in range(0, 1000):
        int_list.append(i)
    correctOrder = True

    is_pass = (int_list.getSize() == 1000)
    assert is_pass == True, "fail the test"

    for i in range(0, 200):
        if int_list.pop() != 999 - i:
            correctOrder = False

    is_pass = correctOrder
    assert is_pass == True, "fail the test"

    is_pass = (int_list.searchLarger(200) == 201)
    assert is_pass == True, "fail the test"

    int_list.insert(7, 801)

    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"

    is_pass = (int_list.getItem(-1) == 799)
    assert is_pass == True, "fail the test"

    is_pass = (int_list.getItem(-4) == 796)
    assert is_pass == True, "fail the test"

    if is_pass == True:
        print("=========== Congratulations! Your have finished exercise 2! ============")


if __name__ == '__main__':
    test()
