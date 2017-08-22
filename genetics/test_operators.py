"""
Unit tests for genetic operators
"""
from unittest.mock import patch

from genetics.operators import point_mutate
from genetics.operators import crossover

from utils.dictionary import reverse
from tree.tree import Tree
from environment.environment import BasicEnvironment

def not_so_random_choice(arr):
    return arr[0]

def choice_leaf(arr):
    return arr[2]

# @patch('genetics.operators.choice', side_effect=not_so_random_choice)
# def test_point_mutation(choice_mock, tree_stub):
    
#     tree = point_mutate(tree_stub)

#     listed_nodes = [(k.id, k.value) for _, k in tree.nodes.items()]

#     assert listed_nodes == [
#         (0, '_diff'),
#         (1, '_diff'),
#         (2, '5'),
#         (3, '10'),
#         (4, '3')
#     ]

#     assert tree_stub.nodes != tree.nodes

# @patch('genetics.operators.choice', side_effect=choice_leaf)
# def test_point_mutation_leaf(choice_mock, tree_stub):
#     tree = point_mutate(tree_stub)

#     listed_nodes = [(k.id, k.value) for _, k in tree.nodes.items()]

#     assert listed_nodes == [
#         (0, '_sum'),
#         (1, '_diff'),
#         (2, '2'),
#         (3, '10'),
#         (4, '3')
#     ]

#     assert tree.nodes != tree_stub.nodes

# def choose_start_node(arr):
#     return arr[1]

# def random_crosspoint_generator():
#     for value in [2,1]:
#         yield value

# @patch('genetics.operators.choice', side_effect=choose_start_node)
# def test_crossover(choice_mock, tree_stub, tree_stub2):
#     child_a, child_b = crossover(tree_stub, tree_stub2)

#     assert str(child_a) == '_sum(_log(_log(10)),5)'
#     assert str(child_b) == '_sum(_diff(10,3),3)'

#     gen = random_crosspoint_generator()

#     def random_crosspoint(_):
#         return next(gen)

#     tree_a = Tree(
#         [(4, 0), (4, 3), (0, 2), (0, 1)],
#         BasicEnvironment().nonterminals,
#         {0: '_sum', 1: 'x', 2: '3', 3: 'x', 4: '_diff'}
#     )

#     tree_b = Tree(
#         [(3, 1), (1, 2), (3, 4), (1, 0)],
#         BasicEnvironment().nonterminals,
#         {0: '2', 1: '_sum', 2: '2', 3: '_sum', 4: '3'}
#     )

#     choice_mock.side_effect = random_crosspoint

#     child_a, child_b = crossover(tree_a, tree_b)

#     assert str(child_a) != str(tree_a)

# def test_subtree_mutation():
#     pass
