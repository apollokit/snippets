#  https://www.educative.io/courses/data-structures-coding-interviews-python/N7jKNEvKrnm
# good animation at the above link
# The basic idea of Kadane’s algorithm is to scan the entire list and at each position find the maximum sum of the sublist ending there. This is achieved by keeping a current_max for the current list index and a global_max. The algorithm is as follows

def find_max_sum_sublist(lst): 
  # use Kadane's alg
  if (len(lst) < 1): 
    return 0;

  curr_max = lst[0];
  global_max = lst[0];
  length_array = len(lst);
  for i in range(1, length_array):
    # if the contributions before elem i are net-negative, then they don't
    # help with maximization. Ignore and start at i
    if curr_max < 0: 
      curr_max = lst[i]
    # see if extending the sublist helps
    else:
      curr_max += lst[i]
    # does the current sublist have a greater sum than any we've seen thus
    # far?
    if global_max < curr_max:
      global_max = curr_max

  return global_max;


lst = [-4, 2, -5, 1, 2, 3, 6, -5, 1];
print("Sum of largest subarray: ", find_max_sum_sublist(lst));