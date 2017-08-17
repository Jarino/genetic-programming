def flat_dfs(hash_map, start_id):
    """
    Perform the depth firts search and return the flat array of visited nodes
    """
    seq = []
    stack = [start_id]

    while len(stack) > 0:
        current_node_id = stack.pop()

        seq.append(current_node_id)

        for child_id in reversed(hash_map[current_node_id]):
            stack.append(child_id)

    return seq
