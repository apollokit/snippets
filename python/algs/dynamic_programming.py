#  https://www.educative.io/courses/data-structures-coding-interviews-python/N7jKNEvKrnm
# good animation at the above link
# The basic idea of Kadane’s algorithm is to scan the entire list and at each position find the maximum sum of the sublist ending there. This is achieved by keeping a current_max for the current list index and a global_max. The algorithm is as follows

def find_max_sum_sublist(lst): 
    # use Kadane's alg
    if (len(lst) < 1): 
        return 0

    curr_max = lst[0]
    global_max = lst[0]
    length_array = len(lst)
    for i in range(1, length_array):
        # if the contributions before elem i are net-negative, then they don't
        # help with maximization. Ignore and start at i
        if curr_max < 0: 
            curr_max = lst[i]
        # seea if extending the sublist helps
        else:
            curr_max += lst[i]
        # does the current sublist have a greater sum than any we've seen thus
        # far?
        if global_max < curr_max:
            global_max = curr_max

    return global_max

def test_find_max_sum_sublist():
    lst = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
    print("Sum of largest subarray: ", find_max_sum_sublist(lst))


def knap_sack_recursive(lookup_table, profits, profits_length, weights, capacity, current_index):
    """
    Finds the maximum value that can be put in a knapsack
    :param profits: The profit that can be gained by each
    :param profits_length: The number of pieces of jewelry
    :param weights: The weight of each piece of jewelry
    :param capacity: The maximum weight that the knapsack can hold
    :param current_index: Current index of the weights
    :return: Maximum value that can be put in a knapsack
    """
    # base checks

    if capacity <= 0 or current_index >= profits_length or current_index < 0:
        return 0

    # if we have already solved the problem, return the result from the table
    if lookup_table[current_index][capacity] != 0:
        return lookup_table[current_index][capacity]

    # recursive call after choosing the element at the current_index
    # if the weight of the element at current_index exceeds the capacity, we shouldn't process this
    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + knap_sack_recursive(
            lookup_table,
            profits,
            profits_length,
            weights,
            capacity - weights[current_index],
            current_index + 1
        )

    # recursive call after excluding the element at the current_index
    profit2 = knap_sack_recursive(lookup_table, profits, profits_length,
                                  weights, capacity, current_index + 1)

    lookup_table[current_index][capacity] = max(profit1, profit2)
    return lookup_table[current_index][capacity]


def knap_sack(profits, profits_length, weights, capacity):
    """
    Finds the maximum value that can be put in a knapsack
    :param profits: The profit that can be gained by each
    :param profits_length: The number of pieces of jewelry
    :param weights: The weight of each piece of jewelry
    :param capacity: The maximum weight that the knapsack can hold
    :return: Maximum value that can be put in a knapsack
    """
    lookup_table = [[0 for x in range(capacity + 1)] for x in range(profits_length + 1)]

    return knap_sack_recursive(lookup_table, profits, profits_length, weights, capacity, 0)

# https://www.educative.io/module/lesson/algorithms-in-python/m77mWZ1lQkr
def count_ways(n):
    """Calculates the number of ways a staircase of n steps can be climbed,
    when we can step you either 1,2, or 3 steps at a time

    :param n: Number of stairs
    :return: Number of ways to climb a stair
    """

    # min table size for storing base cases
    # n+1 to account for 0 step base case
    min_n_table = max(n+1, 3)

    # each entry means: 
    #   index: the number of steps left to ascend (0 means we're on the last step)
    #   value: number of ways to ascend the number of steps left
    ways_per_steps_left_table = [0]*min_n_table

    # if we're already on the last step , then we're there. So, technically,
    # this is a "way" of getting there. We need this base case for the
    # loop below. Seems kind of strange at first, but
    # makes sense after you think about it. If we have one step left, the only
    # way is to take one step, and then the no-op on the last step. So what
    # we're really counting is the no-op at the end, and there was only method
    # of arriving at that
    ways_per_steps_left_table[0] = 1
    # just count the number of ways here 
    ways_per_steps_left_table[1] = 1 # only one step
    ways_per_steps_left_table[2] = 1 + 1  # one step twice, and two steps once
    # (so, two ways of arriving at the no-op)

    for num_steps_left in range(n+1):
        num_ways = 0
        if num_steps_left > 2:
            # three different choices we can make, so we need to count up the
            # number of ways for each of those choices
            # note: we don't add one here because this decision doesn't
            # count as a "way"
            num_ways += ways_per_steps_left_table[num_steps_left-1]
            num_ways += ways_per_steps_left_table[num_steps_left-2]
            num_ways += ways_per_steps_left_table[num_steps_left-3]
            ways_per_steps_left_table[num_steps_left] = num_ways

    return ways_per_steps_left_table[n]



# Driver code to test the above function
if __name__ == '__main__':
    profits = [1, 6, 10, 16]  # The values of the jewelry
    weights = [1, 2, 3, 5]  # The weight of each
    print("Total knapsack profit = ", knap_sack(profits, len(profits), weights, 7))
    print("Total knapsack profit = ", knap_sack(profits, len(profits), weights, 6))
