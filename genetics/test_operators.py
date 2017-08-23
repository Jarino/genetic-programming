"""
Unit tests for genetic operators
"""
from unittest.mock import patch

from rtree.dfs import walk_values
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
def test_point_mutation(choice_mock, test_tree_a):

    gen = choice_generator([1, 0])

    choice_mock.side_effect = lambda x: x[next(gen)]

    mutated = point_mutation(test_tree_a, {
        2: ['xxx']
    })

    assert walk_values(mutated) == [0, 'xxx', 2, 3, 4]


@patch('genetics.operators.choice')
def test_point_mutation(choice_mock, test_tree_a):
    gen = choice_generator([3, 0])

    choice_mock.side_effect = lambda x: x[next(gen)]

    mutated = point_mutation(test_tree_a, {
        0: ['x']
    })

    assert walk_values(mutated) == [0, 1, 2, 'x', 4]