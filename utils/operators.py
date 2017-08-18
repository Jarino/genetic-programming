import math

def c_sum(*args):
    return sum(args)

def c_log(x):
    try:
        return math.log(x)
    except ValueError:
        return 0

def c_div(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 0

def c_prod(x,y):
    return x*y

def c_diff(x,y):
    return x-y