def walk_values(start_node):

    stack = [start_node]
    walk = []

    while len(stack) != 0:
        current_node = stack.pop()
        stack += reversed(current_node.children)
        walk.append(current_node.value)
    
    return walk

def walk_nodes(start_node):

    stack = [start_node]
    walk = []

    while len(stack) != 0:
        current_node = stack.pop()
        stack += reversed(current_node.children)
        walk.append(current_node)
    
    return walk

# TODO
# this is not an DFS actually, so the module should be somehow renamed, or 
# method moved
def walk_nodes_with_parents(start_node):
    stack = [start_node]

    # since this method is (as for now) used solely for crossover operation 
    # and it doesn't make much sense at the root node (since that would 
    # only swap trees, yielding no new individuals to evaluate), we leave
    # out the root node from the walk
    #walk = [(None, start_node)]
    walk = []
    
    while len(stack) != 0:
        current_node = stack.pop()
        stack += reversed(current_node.children)

        for child in current_node.children:
            walk.append((current_node, child))

    return walk
