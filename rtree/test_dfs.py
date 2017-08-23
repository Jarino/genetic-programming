from rtree.dfs import walk_values
from rtree.dfs import walk_nodes_with_parents


def test_dfs(test_root_node):
    walk = walk_values(test_root_node)

    assert walk == [3, 1, 2, 0, 4]

def test_dfs_from_subtree(test_root_node):

    walk = walk_values(test_root_node.children[0])

    assert walk == [1, 2, 0]

def test_dfs_with_parents(test_root_node):
    walk = walk_nodes_with_parents(test_root_node)
    
    values = []

    for parent, child in walk:
        parent_value = None if parent is None else parent.value
        values.append((parent_value, child.value))

    assert values == [(None, 3), (3, 1), (3, 4), (1, 2), (1, 0)]