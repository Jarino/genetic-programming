"""
Unit tests for genetic operators
"""
from unittest.mock import Mock
from unittest.mock import patch

from utils.dfs import walk_values
from genetics.operators import crossover
from genetics.operators import point_mutation


@patch('genetics.operators.choice')
def test_crossover(choice_mock, test_tree_a, test_tree_b):

    gen = choice_generator([0, 2])

    choice_mock.side_effect = lambda x: x[next(gen)]

    child_a, child_b = crossover(test_tree_a, test_tree_b)

    assert walk_values(child_a) == [0, 'd', 'e', 4]
    assert walk_values(child_b) == [
        'a', 'b', 'c', 1, 2, 3
    ]

def choice_generator(values):
    for value in values:
        yield value

@patch('genetics.operators.choice')
def test_point_mutation_node(choice_mock, test_tree_a):

    gen = choice_generator([1, 0])

    choice_mock.side_effect = lambda x: x[next(gen)]

    env = Mock(symbols={
        'xxx': lambda x, y: x
    }, symbols_inv={
        2: ['xxx']
    })

    mutated = point_mutation(test_tree_a, env)

    assert walk_values(mutated) == [0, 'xxx', 2, 3, 4]


@patch('genetics.operators.choice')
def test_point_mutation_leaf(choice_mock, test_tree_a):
    gen = choice_generator([3, 0])

    choice_mock.side_effect = lambda x: x[next(gen)]

    env = Mock(symbols={
        '_vars': lambda: 'x'
    }, symbols_inv={
        0: ['_vars']
    })


    mutated = point_mutation(test_tree_a, env)

    assert walk_values(mutated) == [0, 1, 2, 'x', 4]