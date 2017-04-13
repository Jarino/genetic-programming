"""module docstring"""

from random import randint

def generate(code_length):
    """generate Read linear code"""
    if code_length == 1:
        return [0]

    code = [0] * (code_length + 1)
    upper_bounds = [0] * (code_length + 1)

    upper_bounds[1] = code_length - 1
    code[1] = randint(1, upper_bounds[1])

    for i in range(2, code_length):
        upper_bounds[i] = upper_bounds[i - 1] - code[i - 1]

        if (code_length - i) == upper_bounds[i]:
            code[i] = randint(1, upper_bounds[i])
        else:
            code[i] = randint(0, upper_bounds[i])

    code.pop(0)
    return code

def is_valid(code):
    """checks wheter code is valid read code"""
    if sum(code) != len(code)-1:
        return False

    subcodes = [code[0:i] for i in range(1, len(code))]

    for i, subcode in enumerate(subcodes):
        if sum(subcode) < i+1:
            return False

    return True

def subtree_length(code, position):
    """get lenght of subtree in current position"""
    cumsum = 0

    for i, code_indices in enumerate(range(position, len(code))):
        cumsum += code[code_indices]
        if cumsum == i:
            return i + 1

    return 1
