import pytest

from utils.edges_parser import parse_to_nodes

@pytest.fixture(scope='module')
def test_root_node():
    edges = [(3, 1), (3, 4), (1, 2), (1, 0)]

    root_node, _ = parse_to_nodes(edges)

    return root_node

@pytest.fixture(scope='module')
def tree_with_vars():
    edges = [(3, 1), (3, 4), (1, 2), (1, 0)]

    values = {
        3: '_sum',
        1: '_diff',
        2: 'x',
        0: 'z',
        4: 'y'
    }

    root_node, _ = parse_to_nodes(edges, values)

    return root_node

@pytest.fixture(scope='module')
def tree_with_vars_and_numbers():
    edges = [(3, 1), (3, 4), (1, 2), (1, 0)]

    values = {
        3: '_sum',
        1: '_diff',
        2: 'x',
        0: 'z',
        4: '9'
    }

    root_node, _ = parse_to_nodes(edges, values)

    return root_node

    