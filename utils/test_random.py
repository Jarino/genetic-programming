"""
Unit tests for tree generation
"""

from unittest.mock import patch
from unittest.mock import Mock

import numpy as np

from environment.environment import BasicEnvironment
from utils.random import get_random_tree
from utils.random import assign_random_symbols



def test_basic_tree():
    src, edges = get_random_tree(3, [2])

    assert src == [0, 1, 2, 3, 4, 5, 6]
    assert edges == [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]


# we didn't patched the obvious random.choice because of style of import
# we used in the tree module, see
# http://fgimian.github.io/blog/2014/04/10/using-the-python-mock-library-to-fake-regular-functions-during-tests/
# for reference

def test_assign_random_symbols():
    edges = [(1, 2), (2, 3), (1, 5)]

    def num_gen():
        while True:
            yield '5'

    gen = num_gen()

    env = Mock(symbols={
        'sum': lambda x, y: x + y,
        'log': lambda x: x,
        'int': lambda: next(gen)
    }, 
    symbols_inv={
        2: ['sum'],
        1: ['log'],
        0: ['int']
    })

    values = assign_random_symbols(edges, env)

    assert values == {1: 'sum', 2: 'log', 3: '5', 5: '5'}