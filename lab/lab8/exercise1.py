# Exercise 1: Length of List
# finds the length of a list using a recurisve function
# author: Megan Sorenson

# user-defined functions
def mylen(alist):
    '''
    Finds the length of a list using recursion
    Alist is a list of any type of objects
    Returns an int representing the length of the list
    '''

    if [] == alist:  # base case if list is empty
        return 0
    else:
        alist.pop()
    return 1 + mylen(alist)

# main function


def main():
    '''
    The main function of the program
    Tests the recursive mylen() function using a sample input
    '''
    alist = [43, 76, 97, 86]
    print(mylen(alist))


main()
