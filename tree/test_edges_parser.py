from tree.edges_parser import parse
from tree.edges_parser import parse_to_nodes

def test_edges_parser():
    input_edges = [(1, 2), (1, 3), (3, 4)]

    nodes, hash_map = parse(input_edges)

    assert nodes == [1,2,3,4]
    assert hash_map == {
        1: [2, 3],
        2: [],
        3: [4],
        4: []
    }

def test_parsing_to_nodes_without_values():
    edges = [(3, 1), (3, 4), (1, 2), (1, 0)]

    root_node, nodes = parse_to_nodes(edges)

    assert set([x.value for x in nodes]) == set([0, 1, 2, 3, 4])

def test_parsing_to_nodes_with_values():
    edges = [(3, 1), (3, 4), (1, 2), (1, 0)]

    values = {
        3: 'sum',
        1: 'diff',
        0: 'x',
        2: 'y',
        4: 'z'
    }

    root_node, nodes = parse_to_nodes(edges, values)

    assert set([x.value for x in nodes]) == set(['sum', 'diff', 'x', 'y', 'z'])