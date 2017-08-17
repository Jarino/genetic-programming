from tree.edges_parser import parse
from tree.node import Node

NONTERMINAL = {
    'sum': 2,
    'prod': 2,
    'log': 1,
    'sin': 1
}

class Tree():

    def __init__(self, edges, values=None):
        node_ids, self.hash_map = parse(edges)

        self.root = edges[0][0]

        if values is not None:
            self.nodes = {x:Node(x, value=values[x]) for x in node_ids}
        else:
            self.nodes = {x:Node(x) for x in node_ids}

        
    def flat_dfs(self, start_id):
        seq = []
        stack = [start_id]

        while len(stack) > 0:
            current_node_id = stack.pop()

            seq.append(current_node_id)

            for child_id in reversed(self.hash_map[current_node_id]):
                stack.append(child_id)

        return seq

    def __str__(self):
        stack = []

        for token in reversed(self.flat_dfs(self.root)):

            current_node = self.nodes[token]

            if current_node.value not in NONTERMINAL:
                stack.append(current_node.value)
            else:
                n_arguments = NONTERMINAL[current_node.value]
                operands = [stack.pop() for _ in range(0, n_arguments)]
                stack.append('{}({})'.format(current_node.value, ','.join(operands)))
        
        return stack.pop()
