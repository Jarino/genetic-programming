"""
Contains function for parsing the list of edges into hash data structure
"""

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

    return nodes, hash_map
