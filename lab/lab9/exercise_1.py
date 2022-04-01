# Recursive sorting algorithms
# author: Megan Sorenson
# main function testing written by CMPUT 175

import random
import time

#---------------------------------------#
# Implement Recursive selection sort here.

# n: size of array - index is index of starting element


def recursive_selection_sort(data, data_len, index=0):
    '''
    Recursively sorts a list in descending order using selection sort
    data is a list of int or str that is being sorted
    index is an int representing the beginning index of the list
    returns "Selection Sort Complete" as a str if the list is done being sorted
    otherwise returns None
    '''
    # TODO-Remove pass and fill out the rest.
    # You may use additional user_defined functions if required.

    # Set the base case
    if index == data_len:  # when you reach the end of the list
        return "Selection Sort Complete."

    # Find the minimum index
    maximum_index = index
    for i in range(index + 1, data_len):
        if data[maximum_index] < data[i]:
            maximum_index = i

    # Swap the data
    maximum = data[maximum_index]
    data[maximum_index] = data[index]
    data[index] = maximum
    # Recursively calling selection sort function
    recursive_selection_sort(data, data_len, index + 1)

#---------------------------------------#
# Implement the Recursive merge sort here


def recursive_merge_sort(data):
    '''
    Recursively sorts a list in descending order using merge sort
    data is a list of integers or strings that are being sorted
    returns a the data list if it only contains one item
    otherwise returns the merged left and right lists in descending order
    '''
    # TODO-Remove pass and fill out the rest.
    # You may use additional user_defined functions if required.

    # Set the base case
    if len(data) <= 1:
        return data

    # Find the middle of the data list
    middle_index = len(data) // 2

    # Recursively calling merge sort function for both half of the data list
    left = recursive_merge_sort(data[:middle_index])
    right = recursive_merge_sort(data[middle_index:])

    # merge the two halves of the data list and return the data list
    return merge(left, right)


def merge(left, right):
    '''
    Merges two lists in descending order for a recursive merge sort 
    left is the left side of the list
    right is the right side of the list
    returns a merged list in descending order
    '''
    # set initial indexes to iterate as items are removed from the left and right lists
    left_index = 0
    right_index = 0

    merged_list = []
    # while one of the lists hasn;t been completely iterated over,
    #   find which list has the higher number at index
    #   append higher number to merged_list
    #   increment appropriate index
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1

    # add remaining elements of left and right
    # only one should still have elements
    merged_list += left[left_index:]
    merged_list += right[right_index:]

    return merged_list


#---------------------------------------#
if __name__ == "__main__":
    # Define the list of random numbers
    random_list = [random.randint(1, 1000) for i in range(500)]
    list_len = len(random_list)
    ascending_list = sorted(random_list)
    descending_list = sorted(random_list, reverse=True)

    # Calculate the execution time to sort a list of random numbers #
    random_list_ = random_list.copy()  # make a copy to save the unsorted list
    start_sel = time.time()
    recursive_selection_sort(random_list_, list_len)
    end_sel = time.time()

    start_merge = time.time()
    recursive_merge_sort(random_list)
    end_merge = time.time()

    # Print the rsults execution time to sort a list of random numbers
    print('The execution time: to sort a random list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))

    # Calculate the execution time to sort a list of intergers already sorted in ascending order #
    ascending_list_ = ascending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(ascending_list_, list_len)
    end_sel = time.time()

    start_merge = time.time()
    recursive_merge_sort(ascending_list)
    end_merge = time.time()

    # Print the rsults execution time to sort a list of intergers already sorted in ascending order
    print('The execution time: to sort a ascending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))

    # Calculate the execution time to sort a list of intergers already sorted in descending order #
    descending_list_ = descending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(descending_list_, list_len)
    end_sel = time.time()

    start_merge = time.time()
    recursive_merge_sort(descending_list)
    end_merge = time.time()

    # Print the rsults execution time to sort a list of intergers already sorted in descending order
    print('The execution time: to sort a descending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))
