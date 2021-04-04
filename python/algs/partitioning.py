def three_way_partition(lst):
    """
    A 3-way partitioning algorithm for lists

    A function to solve Dutch National Flag Problem

    :param lst: A list of integers 0,1,2
    :return: A list of solved Dutch National Flag Problem
    """

    size = len(lst)
    i = 0
    mid = 0
    j = size - 1

    while mid <= j:
        if lst[mid] == 0:
            lst[i], lst[mid] = lst[mid], lst[i]
            i += 1
            mid += 1
        elif lst[mid] == 2:
            lst[mid], lst[j] = lst[j], lst[mid]
            j -= 1
        elif lst[mid] == 1:
            mid += 1

    return lst


# Driver to test above code
if __name__ == '__main__':

    lst = [2, 0, 0, 1, 2, 1]

    print(dutch_national_flag(lst))