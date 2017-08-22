from rtree.dfs import walk_values


def test_dfs(test_root_node):
    walk = walk_values(test_root_node)

    assert walk == [3, 1, 2, 0, 4]

def test_dfs_from_subtree(test_root_node):

    walk = walk_values(test_root_node.children[0])

    assert walk == [1, 2, 0]