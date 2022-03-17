# Exercise 2: Integer Division
# finds the integer result of divident/divisor using recursion
# author: Megan Sorenson

# user-defined functions
def intDivision(dividend, divisor):
    '''
    Performs integer division using the given inputs
    dividend is an int representing the numerator of the interger division
    divisor is an int representing the denominator of the integer division
    Returns an int representing the result of the integer division
    '''
    if dividend < divisor:  # base case where divisor cannot be subtracted from dividend
        return 0

    return 1 + intDivision(dividend - divisor, divisor)

# main function


def main():
    '''
    Main function of the program
    Tests the intDivision() function using test inputs
    '''
    n = int(input('Enter an integer dividend: '))
    m = int(input('Enter an integer divisor: '))
    print('Integer division', n, '//', m, '=', intDivision(n, m))


main()
