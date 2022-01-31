from stack1 import Stack


def parChecker(symbolString):
    # initialization
    s = Stack()
    index = 0
    balanced = True

    # start the iteration
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not match(top, symbol):
                    balanced = False
        index += 1


def match(open_bracket, close_bracket):
    pass
