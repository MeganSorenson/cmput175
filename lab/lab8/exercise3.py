# Exercise 3: Sums of Digits of Integer
# computes the sum of digits of aninteger using recursion
# author: Megan Sorenson

# user-defined functions
def sumdigits(number):
    '''
    Calculates the sum of digits of an integer
    number is an integer whose digtis are being summed
    returns an int representing the sum of digits of number
    '''
    # check the validity of the input
    assert isinstance(
        number, int) and number >= 0, 'Error: number must be a positive integer'

    number = list(str(number))
    digit = number.pop()

    if [] == number:  # base case where all digits are accounted for
        return int(digit)

    return int(digit) + sumdigits(int(''.join(number)))

# main function


def main():
    '''
    Main function of the program
    tests the sumdigits() functions using a sample input
    '''
    number = int(input('Enter a number: '))
    print(sumdigits(number))


main()
