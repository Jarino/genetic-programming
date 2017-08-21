"""
Module containing functions for genetic operations
"""
from inspect import signature as sg
from random import choice

from tree.tree import Tree
from tree.node import Node

def point_mutate(tree, nonterminals_rev, terminals):
    # choose random node
    node_id = choice(tree.node_ids)
    
    # determine whether it is leaf or node
    is_leaf = len(tree.hash_map[node_id]) == 0

    if is_leaf:
        # pick random terminal
        new_symbol = choice(terminals)
    else:
        # check how many arguments it has to take
        old_symbol = tree.nodes[node_id]
        n_args = len(sg(tree.nonterminals[old_symbol.value]).parameters)
        print(nonterminals_rev)
        new_symbol = choice(nonterminals_rev[n_args])

    mutated_tree = tree.copy()

    mutated_tree.nodes.update({node_id: Node(node_id, new_symbol)})
    print('New symbol: ', new_symbol)
    print('before: ', tree.nodes[node_id].value)
    print('after:  ', mutated_tree.nodes[node_id].value)

    return mutated_tree

