"""
Unit tests for tree generation
"""

from unittest.mock import patch
from unittest.mock import Mock

import numpy as np

from environment.environment import BasicEnvironment
from utils.random import get_random_tree
from utils.random import choose_child
from utils.random import assign_random_symbols


def not_so_random_permutation(length):
    return np.array(range(0, length))

def not_so_random_choice(arr):
    return arr[-1]

def choice_generator(length):
    for i in range(0, length):
        yield i


@patch('numpy.random.permutation', side_effect=not_so_random_permutation)
@patch('utils.random.choice', side_effect=not_so_random_choice)
def test_basic_tree(permutation_mock, choice_mock):
    src, edges = get_random_tree(5, 2)

    assert src == [4, 3, 2, 1, 0]
    assert edges == [(4, 3), (3, 2), (2, 1), (1, 0)]


# we didn't patched the obvious random.choice because of style of import
# we used in the tree module, see
# http://fgimian.github.io/blog/2014/04/10/using-the-python-mock-library-to-fake-regular-functions-during-tests/
# for reference
@patch('utils.random.choice')
def test_choose_child_upper_bound(choice_mock):
    """
    Tests whether function returns child which do not violate the upper bound
    of number of children
    """
    generator = choice_generator(3)

    def choice_return_value(arr):
        return next(generator)

    choice_mock.side_effect = choice_return_value

    child = choose_child([0,1,2], [
        (0,1), (0,2), (1,3), (1,2), (1,1), 
    ], 2)

    assert child == 2

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