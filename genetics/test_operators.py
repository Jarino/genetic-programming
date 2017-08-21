"""
Unit tests for genetic operators
"""
from unittest.mock import patch

from genetics.operators import point_mutate

from utils.dictionary import reverse

def not_so_random_choice(arr):
    return arr[0]

def choice_leaf(arr):
    return arr[2]

@patch('genetics.operators.choice', side_effect=not_so_random_choice)
def test_point_mutation(choice_mock, tree_stub):
    
    tree = point_mutate(tree_stub)

    listed_nodes = [(k.id, k.value) for _, k in tree.nodes.items()]

    assert listed_nodes == [
            (0, '_diff'),
            (1, '_diff'),
            (2, '5'),
            (3, '10'),
            (4, '3')
        ]

    assert tree_stub.nodes != tree.nodes

@patch('genetics.operators.choice', side_effect=choice_leaf)
def test_point_mutation_leaf(choice_mock, tree_stub):
    tree = point_mutate(tree_stub)

    listed_nodes = [(k.id, k.value) for _, k in tree.nodes.items()]

    assert listed_nodes == [
            (0, '_sum'),
            (1, '_diff'),
            (2, '2'),
            (3, '10'),
            (4, '3')
        ]
    
    assert tree.nodes != tree_stub.nodes

def test_subtree_mutation():
    pass

def test_crossover():
    pass
