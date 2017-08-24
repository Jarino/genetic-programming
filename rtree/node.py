from copy import deepcopy

from utils.dfs import walk_nodes


class Node():

    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

    def add_child(self, child):
        self.children.append(child)
    
    def __str__(self):
        stack = []

        for current_node in reversed(walk_nodes(self)):
            if len(current_node.children) == 0:
                stack.append(current_node.value)
            else:
                n_arguments = len(current_node.children)
                operands = [stack.pop() for _ in range(0, n_arguments)]
                stack.append('{}({})'.format(current_node.value, ','.join(operands)))
        
        return stack.pop()

    def __call__(self, nonterminals, terminals):
        return eval(str(self), {**nonterminals, **terminals} )

    def copy(self):
        return deepcopy(self)
