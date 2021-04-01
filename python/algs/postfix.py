
import operator

OPERATORS = {
    '+': operator.add, 
    '-': operator.sub, 
    '*': operator.mul, 
    '/': operator.truediv
}


class MyStack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()

# my implementation of https://www.educative.io/courses/data-structures-coding-interviews-python/B81w73oM5xX
def evaluate_post_fix(exp):
    
    # stores the numerical values we will operate on
    numbers_stack = MyStack()

    tokens = exp.split(' ')

    while len(tokens) > 0:
        token = tokens.pop(0)

        if token in OPERATORS.keys():
            op_func = OPERATORS[token]
            right = numbers_stack.pop()
            left = numbers_stack.pop()
            result = op_func(left, right)
            numbers_stack.push(result)

        else:
            numbers_stack.push(int(token))

    assert numbers_stack.size() == 1
    return numbers_stack.pop()

print(evaluate_post_fix('9 2 1 * - 8 - 4 +'))