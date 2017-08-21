import pytest

from tree.tree import Tree

@pytest.fixture(scope="session")
def tree_stub():
    edges = [(0, 1), (1, 3), (1, 4), (0, 2)]
    return Tree(edges, {
            '_log': lambda x: x,
            '_sum': lambda x, y: x + y,
            '_diff': lambda x, y: x - y
        }, {
            0: '_sum',
            1: '_diff',
            2: '5',
            3: '10',
            4: '3'
        })
