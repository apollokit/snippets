def right_rotate(lst, k):
    """right rotate a list by k steps
    
    change [10, 20, 30, 40, 50]
    to [40, 50, 10, 20, 30]    
    """
    # get rotation index
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    return lst[-k:] + lst[:-k]


print(right_rotate([10, 20, 30, 40, 50], 3))