"""Modul ktory bude obsahovat metody tykajuce sa """

import random

TERMINALS = ['x', *list(range(1, 10))]
NONTERMINALS = ['+', '-', '*', '/']

def assign_symbols(code):
    """assign symbols to read's code"""
    res = []
    for index, symbol in enumerate(code):
        if symbol[0] == 0:
            res.append((symbol[0], random.choice(TERMINALS)))
        else:
            res.append((symbol[0], random.choice(NONTERMINALS)))
    return res
    