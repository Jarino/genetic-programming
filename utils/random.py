"""
Functions related to generation of random trees.
"""

from random import choice
from functools import reduce
from collections import Counter

import numpy as np

from utils.dictionary import reverse

def choose_child(options, edges, child_limit):
    """
    Choose random child from set of options such that given node did not
    exceed the child limit
    """
    count = child_limit

    while count >= child_limit:
        selected = choice(options)

        count = reduce( (
            lambda cum, item: cum + 1 if item[0] == selected else cum + 0
        ), edges, 0)
    
    return selected


def get_random_tree(n_nodes, child_limit):
    """
    Generate random tree containing n_nodes. The depth is not limited.
    chlid_limit limits the number of child each node can have. 

    Returns simple representation of tree - list of nodes and list of edges

    Implemented by this:
    https://nokyotsu.com/qscripts/2008/05/generating-random-trees-and-connected.html
    """
    nodes = np.random.permutation(n_nodes).tolist()
    # choose the root
    src = [nodes.pop()]
    edges = []

    while len(nodes) > 0:
        # since at the first iteration the src array contains only root, we can
        # be sure it won't be detached
        parent = choose_child(src, edges, child_limit)
        child = nodes.pop()
        edges.append((parent, child))
        src.append(child)
    return src, edges

def assign_random_symbols(edges, env):
    """
    Assign random terminals to leafs and non terminals to nodes
    """
    # nonterminals_rev = reverse(nonterminals)

    parents = [x[0] for x in edges]
    p_occurencies = Counter(parents)

    children = set([x[1] for x in edges])
    leaves = children - set(parents)

    values = {}

    for parent in parents:
        n_args = p_occurencies[parent]
        operator = choice(env.symbols_inv[n_args])
        values[parent] = operator

    for leaf in leaves:
        # symbol which takes no arguments is considered terminal
        term = choice(env.symbols_inv[0])
        # call the generator of the terminal
        values[leaf] = env.symbols[term]()

    return values
