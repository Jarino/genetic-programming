"""
Module containing functions for genetic operations
"""
from random import choice

from rtree.dfs import walk_nodes_with_parents
from rtree.dfs import walk_nodes


def crossover(tree_a, tree_b):
    child_a = tree_a.copy()
    child_b = tree_b.copy()

    _switch_subtrees(child_a, child_b)
    
    return child_a, child_b

def _switch_subtrees(tree_a, tree_b):
    tree_a_nodes = walk_nodes_with_parents(tree_a)
    tree_b_nodes = walk_nodes_with_parents(tree_b)

    parent_a, child_a = choice(tree_a_nodes)
    parent_b, child_b = choice(tree_b_nodes)

    index_to_replace = parent_a.children.index(child_a)
    parent_a.children[index_to_replace] = child_b

    index_to_replace = parent_b.children.index(child_b)
    parent_b.children[index_to_replace] = child_a


def point_mutation(tree, symbols):
    mutated_tree = tree.copy()

    nodes = walk_nodes(mutated_tree)

    chosen = choice(nodes)

    chosen.value = choice(symbols[len(chosen.children)])

    return mutated_tree