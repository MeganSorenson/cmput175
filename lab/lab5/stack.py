# ----------------------------------------------------
# Stack implementation #2
# (Top of stack corresponds to back of list)
#
# Author: CMPUT 175 team
# Updated by:
# ----------------------------------------------------

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def pop(self):
        try:
            last_item = self.items.pop()
            return last_item
        except IndexError:
            raise Exception('Cannot go back.')

    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def peek(self):
        try:
            top_item = self.items[len(self.items)-1]
            return top_item
        except IndexError:
            raise Exception('Cannot go forward.')

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)

    def __str__(self):
        stackAsString = ''
        for item in self.items:
            stackAsString += item + ' '
        return stackAsString

    def clear(self):
        # TO DO: complete method according to updated ADT
        if len(self.items) != 0:
            self.items = []
