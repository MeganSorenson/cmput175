# Exercise 5: Binary Search
# recursive binary search that finds and returns the position of the key in a list using recursion
# author: Megan Sorenson

# user-defined functions
def binary_search2(key, alist, low, high):
    '''
    Finds and returns the position of key in alist
    or returns 'Item is not in the list'
    key is the target int that we are looking for
    alist is a list of valid ints that is searched
    low is the lowest index of a list
    high is the highest index of a list
    '''
    guess = (low + high) // 2
    if alist[guess] == key:
        return low
    elif low != high:
        if key < alist[guess]:
            return binary_search2(key, alist, low, guess - 1)
        else:
            return binary_search2(key, alist, guess + 1, high)
    else:
        return 'Item is not in the list'


# main function


def main():
    '''
    Main function of the program
    tests the binary2() function with a sample input
    '''
    some_list = [-8, -2, 1, 3, 5, 7, 9]
    print(binary_search2(9, some_list, 0, len(some_list) - 1))
    print(binary_search2(-8, some_list, 0, len(some_list) - 1))
    print(binary_search2(4, some_list, 0, len(some_list) - 1))


main()
