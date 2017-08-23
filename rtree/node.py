from copy import deepcopy

from rtree.dfs import walk_nodes


class Node():

    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

    def add_child(self, child):
        self.children.append(child)
    
    def to_expression(self, nonterminals):
        stack = []

        for current_node in reversed(walk_nodes(self)):
            if current_node.value not in nonterminals:
                stack.append(current_node.value)
            else:
                n_arguments = len(current_node.children)
                operands = [stack.pop() for _ in range(0, n_arguments)]
                stack.append('{}({})'.format(current_node.value, ','.join(operands)))
        
        return stack.pop()

    def __call__(self, nonterminals, terminals):
        expression = self.to_expression(nonterminals)
        return eval(expression, {**nonterminals, **terminals} )

    def copy(self):
        return deepcopy(self)
