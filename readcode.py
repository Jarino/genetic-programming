"""module docstring"""

from symbols import assign_symbols

from random import choice
from random import randint

def generate_with_symbols(code_length):
    """generate read's linear code with symbols assigned"""
    t = generate(code_length)
    return assign_symbols(t)

def generate(code_length):
    """generate Read linear code. Generate only trees with binary operations"""
    if code_length == 1:
        return [(0, None)]

    code = [0] * (code_length + 1)
    upper_bounds = [0] * (code_length + 1)

    upper_bounds[1] = code_length - 1
    code[1] = (randint(1, min(upper_bounds[1], 2)), None)

    for i in range(2, code_length):
        upper_bounds[i] = upper_bounds[i - 1] - code[i - 1][0]

        if (code_length - i) == upper_bounds[i]:
            code[i] = (randint(1, min(upper_bounds[i], 2)), None)
        else:
            code[i] = (0, None)

    code[code_length] = (0, None)
    code.pop(0)
    return code

def is_valid(code):
    """checks wheter code is valid read code"""
    if sum([x[0] for x in code]) != len(code)-1:
        return False

    subcodes = [code[0:i] for i in range(1, len(code))]

    for i, subcode in enumerate(subcodes):
        if sum([x[0] for x in subcode]) < i+1:
            return False

    return True

def subtree_length(code, position):
    """get lenght of subtree in current position"""
    cumsum = 0

    for i, code_indices in enumerate(range(position, len(code))):
        cumsum += code[code_indices][0]
        if cumsum == i:
            return i + 1

    return 1

def parse(code):
    """create string from code"""
    stack = []
    for node in reversed(code):
        if node[0] == 0:
            stack.append(node[1])

        if node[0] == 2:
            stack.append('(%s%s%s)'%(stack.pop(), node[1], stack.pop()))

        if node[0] == 1:
            stack.append('(%s(%s))'%(node[1], stack.pop()))
    return stack.pop()
