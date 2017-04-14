"""Modul ktory bude obsahovat metody tykajuce sa """

import random

VARIABLES = ['x']
TERMINALS = [*list(range(1, 5))]
UNARY = ['']
BINARY = ['+', '-', '*', '/']

def assign_symbols(code):
    """assign symbols to read's code"""
    res = []
    for symbol in code:
        if symbol[0] == 0:
            res.append((symbol[0], random.choice(random.choice([VARIABLES, TERMINALS]))))
        if symbol[0] == 1:
            res.append((symbol[0], random.choice(UNARY)))
        if symbol[0] == 2:
            res.append((symbol[0], random.choice(BINARY)))
    return res
