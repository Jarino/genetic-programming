"""
Contains function for parsing the list of edges into hash data structure
"""

from rtree.node import Node

def parse(edges):
    """
    Parse the list of edges (list of tuples) into the hash map and set of
    nodes
    """
    nodes = set([y for x in edges for y in x])
    hash_map = {}

    for node in nodes:
        hash_map[node] = []

    for parent, child in edges:
        if len(hash_map[parent]) == 0:
            hash_map[parent] = [child]
        else:
            hash_map[parent].append(child)

    return list(nodes), hash_map

def parse_to_nodes(edges, values=None):
    nodes = {}

    if values is None:
        values = {x:x for x in set([y for x in edges for y in x])}

    root = (set([x[0] for x in edges]) - set([x[1] for x in edges])).pop()

    for parent, child in edges:
        if parent not in nodes:
            nodes[parent] = Node(values[parent])
        if child not in nodes:
            nodes[child] = Node(values[child])

        nodes[parent].add_child(nodes[child])

    return nodes[root], [v for _, v in nodes.items()]
    
