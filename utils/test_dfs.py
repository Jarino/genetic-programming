from utils.dfs import walk_values
from utils.dfs import walk_nodes_with_parents


def test_dfs(test_root_node):
    walk = walk_values(test_root_node)

    assert walk == [3, 1, 2, 0, 4]

def test_dfs_from_subtree(test_root_node):

    walk = walk_values(test_root_node.children[0])

    assert walk == [1, 2, 0]

def test_dfs_with_parents(test_root_node):
    walk = walk_nodes_with_parents(test_root_node)
    
    values = [(x.value, y.value) for x, y in walk]

    assert values == [(3, 1), (3, 4), (1, 2), (1, 0)]