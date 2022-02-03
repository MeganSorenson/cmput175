from stack2 import Stack


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

    if balanced and s.isEmpty():
        # it is important to check both conditions
        # becasue there could be an opening bracket for which there is no closing bracket
        # the second condition ensures that the number of open brackets match the number oof closing beackets
        return True
    else:
        return False


def match(open_bracket, close_bracket):
    # return True is open bracket matches up to its corresponding closing bracket
    # False otherwise
    opens = '([{'
    closers = ')]}'
    if opens.index(open_bracket) == closers.index(close_bracket):
        return True
    else:
        return False


def main():
    symbolString = input('enter symbol > ')
    print(parChecker(symbolString))


main()
