import pytest

from rtree.node import Node
from utils.edges_parser import parse_to_nodes

@pytest.fixture(scope='session')
def test_tree_a():
    edges = [(0, 1), (1, 2), (1, 3), (0, 4)]

    root_node, _ = parse_to_nodes(edges)

    return root_node

@pytest.fixture(scope='session')
def test_tree_b():
    edges = [('a', 'b'), ('b', 'c'), ('b', 'd'), ('d', 'e')]

    root_node, _ = parse_to_nodes(edges)

    return root_node












