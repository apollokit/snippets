
# Floyd's Cycle Finding Algorithm
# from https://www.educative.io/courses/data-structures-coding-interviews-python/m7yj6NGOyjp
# see
# https://www.codingninjas.com/blog/2020/09/09/floyds-cycle-detection-algorithm/
def detect_loop(lst):
    # Keep two iterators
    onestep = lst.get_head()
    twostep = lst.get_head()
    while onestep and twostep and twostep.next_element:
        onestep = onestep.next_element  # Moves one node at a time
        twostep = twostep.next_element.next_element  # Skips a node
        if onestep == twostep:  # Loop exists
            return True
    return False