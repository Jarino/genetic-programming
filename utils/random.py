"""
Functions related to generation of random trees.
"""

from random import choice
from functools import reduce
from itertools import count
from collections import Counter

import numpy as np

from utils.dictionary import reverse


def get_random_tree(max_depth, arities):
    """
    Generate random tree of given depth with randomly chosen arities from
    provided list of all possible arities.

    Returns tuple - list of nodes and list of edges
    """
    new_id = count()
    root = next(new_id) 
    edges = []
    nodes = [root]
    l_queue = [root]

    for _ in range(1, max_depth):
        queue = l_queue[:]
        l_queue = []
        while len(queue) > 0:
            parent = queue.pop(0)

            arity = choice(arities)

            for _ in range(0, arity):
                new_node = next(new_id)
                nodes.append(new_node)
                edges.append((parent, new_node))
                l_queue.append(new_node)

    return nodes, edges

def assign_random_symbols(edges, env):
    """
    Assign random terminals to leafs and non terminals to nodes
    """

    parents = [x[0] for x in edges]
    p_occurencies = Counter(parents)

    children = set([x[1] for x in edges])
    leaves = children - set(parents)

    values = {}

    if len(edges) == 0:
        term = choice(env.symbols_inv[0])
        values[0] = env.symbols[term]()

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
