
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
    operands_stack = MyStack()

    tokens = exp.split(' ')

    while len(tokens) > 0:
        token = tokens.pop(0)

        if token in OPERATORS.keys():
            op_func = OPERATORS[token]
            right = operands_stack.pop()
            left = operands_stack.pop()
            result = op_func(left, right)
            operands_stack.push(result)

        else:
            operands_stack.push(int(token))

    assert operands_stack.size() == 1
    return operands_stack.pop()

print(evaluate_post_fix('9 2 1 * - 8 - 4 +'))