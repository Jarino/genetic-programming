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


