from typing import Any, Optional, Tuple

def binary_search(lst, val) -> Tuple[int, bool]:
    """My implementation of binary search
    
    Args:
        lst: sorted list
        val: the value to search for
    
    Returns:
        the index of the found value, and boolean indicating whether the value
        is found or not. If not found, the index will correspond to the
        closest value (either greater or lower)
    """

    left = 0
    right = len(lst)-1

    found = False
    while left <= right:
        mid = left + (right-left) // 2
        if lst[mid] == val:
            found = True 
            break
        elif lst[mid] < val:
            left = mid + 1
        else:
            right = mid - 1

    return mid, found

if __name__ == "__main__":

    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(lst)
    print(len(lst))
    print(binary_search(lst, -1))
