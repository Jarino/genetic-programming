from tree.edges_parser import parse

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
