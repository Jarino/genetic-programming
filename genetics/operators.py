"""
Module containing functions for genetic operations
"""
from random import choice

from utils.dfs import walk_nodes_with_parents
from utils.dfs import walk_nodes


def crossover(tree_a, tree_b):
    args = [tree_a.copy(), tree_b.copy()]

    # this is a way too shitty way to check, but it fulfills its purpouse:
    # if node has zero number of children, it will be first and _switch_subtrees
    # subroutine then handle the special case
    args.sort(key=lambda x: len(x.children)) 
   
    _switch_subtrees(*args)

    return args

def _switch_subtrees(tree_a, tree_b):
    tree_a_nodes = walk_nodes_with_parents(tree_a)
    tree_b_nodes = walk_nodes_with_parents(tree_b)

    if len(tree_a_nodes) == 0 and len(tree_b_nodes) == 0:
        return 

    if len(tree_a_nodes) == 0:
        parent_b, child_b = choice(tree_b_nodes)
        index_to_replace = parent_b.children.index(child_b)

        parent_b.children[index_to_replace] = tree_a
        tree_a = child_b
        return

    parent_a, child_a = choice(tree_a_nodes)
    parent_b, child_b = choice(tree_b_nodes)

    index_to_replace = parent_a.children.index(child_a)
    parent_a.children[index_to_replace] = child_b

    index_to_replace = parent_b.children.index(child_b)
    parent_b.children[index_to_replace] = child_a


def point_mutation(tree, env):
    """
    TODO: rewrite to per node based evaluation of mutation probability, or?
    """
    mutated_tree = tree.copy()

    nodes = walk_nodes(mutated_tree)

    chosen = choice(nodes)

    n_children = len(chosen.children)
    is_leaf = n_children == 0

    if is_leaf:
        # we need to call generator in this case
        gen_name = choice(env.symbols_inv[0])
        chosen.value = env.symbols[gen_name]()
    else:
        chosen.value = choice(env.symbols_inv[len(chosen.children)])

    return mutated_tree
