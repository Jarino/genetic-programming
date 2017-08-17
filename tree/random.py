"""
An attempt to implement the generation of random trees using the composite
pattern and this link: 
https://nokyotsu.com/qscripts/2008/05/generating-random-trees-and-connected.html

TODO:
- select random node from graph
- limit generation to specific number of children
"""

from random import choice
from functools import reduce

import numpy as np

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

def assign():
    """
    Assign random terminals to leafs and non terminals to nodes
    """
    raise NotImplementedError