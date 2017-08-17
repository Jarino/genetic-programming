from tree.search import flat_dfs
from tree.tree import Tree

def test_flat_dfs():
    """
    test the iterative depth first search of the tree
    """
    hash_map = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [], 6: []}

    search_sequence = flat_dfs(hash_map, 1)

    assert search_sequence == [1, 2, 4, 5, 3, 6]