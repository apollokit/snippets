from typing import List, Any

#  https://www.educative.io/module/lesson/algorithms-in-python/YMqEnMo9yKK
def selection_sort(lst):
    """
    Selection sort function
    :param lst: List of integers
    """

    # Traverse through all lst elements
    for i in range(len(lst)):
        # Find the minimum element in unsorted lst
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j

        # Swap the found minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]

#  https://www.educative.io/module/lesson/algorithms-in-python/YMqEnMo9yKK
def bubble_sort(lst):
    """
    Bubble sort function
    :param lst: lst of unsorted integers
    """

    # Traverse through all list elements
    for i in range(len(lst)):

        # Last i elements are already in place
        for j in range(0, len(lst) - i - 1):

            # Traverse the list from 0 to size of lst - i - 1
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

#  https://www.educative.io/module/lesson/algorithms-in-python/YMqEnMo9yKK
def insertion_sort(lst):
    """
    Insertion sort function

    similar to the way you would organize an unsorted set of manila folders

    :param lst: lst of unsorted integers
    """

    # Traverse through 1 to len(lst)
    for i in range(1, len(lst)):

        key = lst[i]

        # Move elements of lst greater than key, to one position ahead
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key


# inspiration from: https://www.educative.io/module/lesson/algorithms-in-python/R10my26rQl0
def merge_sort(lst: List[Any]):
    """Merge sort in place"""

    # handle base cases
    if len(lst) == 1:
        return
    # technically we can handle this with another recursive call, but more
    # efficient to just do it here
    elif len(lst) == 2:
        if lst[0] > lst[1]:
            # swap
            tmp = lst[0]
            lst[0] = lst[1]
            lst[1] = tmp
        return

    # floor divide for midpoint
    mid = len(lst) // 2
    left = lst[0:mid]
    right = lst[mid:]

    # divide and conquer
    merge_sort(left)
    merge_sort(right)

    # merge 
    ileft = 0
    iright = 0
    imerged = 0

    merged = [0]*len(lst)

    # merge them
    while ileft < len(left) and iright < len(right):
        if left[ileft] <= right[iright]:
            lst[imerged] = left[ileft]
            ileft += 1
        else:
            lst[imerged] = right[iright]
            iright += 1
        imerged += 1

    # the stragglers must be punished
    while ileft < len(left):
        lst[imerged] = left[ileft]
        ileft += 1
        imerged += 1
    while iright < len(right):
        lst[imerged] = right[iright]
        iright += 1
        imerged += 1



if __name__ == "__main__":

    lst = [3, 2, 8, 1, 7, 5, 4, 6, 9]
    print(lst)
    merge_sort(lst)
    print(lst)
