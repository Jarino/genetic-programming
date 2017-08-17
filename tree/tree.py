from tree.edges_parser import parse
from tree.search import flat_dfs
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


    def __str__(self):
        stack = []

        for token in reversed(flat_dfs(self.hash_map, self.root)):

            current_node = self.nodes[token]

            if current_node.value not in NONTERMINAL:
                stack.append(current_node.value)
            else:
                n_arguments = NONTERMINAL[current_node.value]
                operands = [stack.pop() for _ in range(0, n_arguments)]
                stack.append('{}({})'.format(current_node.value, ','.join(operands)))
        
        return stack.pop()
