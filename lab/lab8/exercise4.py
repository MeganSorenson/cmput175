# Exercise 4: Rerse Integer
# displays the digits of an integer value in reverse order on the console using recursion
# author: Megan Sorenson

# user-defined functions
def reverseDisplay(number):
    '''
    Displays the digits of an integer in reverse order
    number is an int whose digits will be reversed
    returns NoneType
    '''
    assert isinstance(
        number, int) and number >= 0, 'Error: number must be a positive integer'

    number = list(str(number))
    digit = number.pop()

    if len(number) == 0:  # base case when all digits have been reversed
        print(digit)
    else:
        print(digit, end='')
        reverseDisplay(int(''.join(number)))

# main function


def main():
    '''
    Main function of the program
    tests the reverseDisplay() function using a sample input
    '''
    number = int(input('Enter a number: '))
    reverseDisplay(number)


main()
