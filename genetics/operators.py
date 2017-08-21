"""
Module containing functions for genetic operations
"""
from inspect import signature as sg
from random import choice

from tree.tree import Tree
from tree.node import Node

def point_mutate(tree):
    # choose random node
    node_id = choice(tree.node_ids)
    
    # determine whether it is leaf or node
    is_leaf = len(tree.hash_map[node_id]) == 0

    if is_leaf:
        # pick random terminal
        new_symbol = choice(tree.environment.terminals)
    else:
        # check how many arguments it has to take
        old_symbol = tree.nodes[node_id]
        n_args = len(sg(tree.environment.nonterminals[old_symbol.value]).parameters)
        # and pick random nonterminal
        new_symbol = choice(tree.environment.reversed_n_args[n_args])

    mutated_tree = tree.copy()

    mutated_tree.nodes.update({node_id: Node(node_id, new_symbol)})

    return mutated_tree

