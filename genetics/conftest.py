import pytest

from tree.tree import Tree
from environment.environment import BasicEnvironment

@pytest.fixture(scope="session")
def tree_stub():
    edges = [(0, 1), (1, 3), (1, 4), (0, 2)]
    return Tree(edges, BasicEnvironment(), {
            0: '_sum',
            1: '_diff',
            2: '5',
            3: '10',
            4: '3'
        })
