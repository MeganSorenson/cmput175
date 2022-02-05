# implementation of the stack ADT

class Stack:
    # we are going to use a list
    def __init__(self):
        self.items = []

    def push(self, item):
        # size of list - 1 is the top of the stack (right side)
        self.items.append(item)

    def pop(self):
        # pop from right side
        return self.items.pop()

    def peek(self):
        # just look at top of stack
        return self.items[-1]

    def isEmpty(self):
        # returns T or F depending on if stack is empty or not
        return self.items == []

    def size(self):
        # returns length of the stack
        return len(self.items)

    def reset(self):
        # reset stack to be empty list
        self.items = []

    def __str__(self):
        # returns the string representation of the object
        return str(self.items)

    def show(self):
        print(self.items)  # print calls __str__ automatically


if __name__ == '__main__':
    # testing the class Stack
    s = Stack()
    s.push('first')
    s.push('second')
    s.push('third')
    s.show()

    print(s.pop())
    s.show()

    print(s.peek())
    s.show()

    s.reset()
    print(s.size())
    s.show()
