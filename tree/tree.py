from inspect import signature as sg
from copy import deepcopy


from randomdict import RandomDict

from tree.edges_parser import parse
from tree.search import flat_dfs
from tree.node import Node

from utils.dictionary import convert_to_args_n

class Tree():

    def __init__(self, edges, nonterminals, values=None):
        self.node_ids, self.hash_map = parse(edges)
        self.nonterminals = nonterminals
        self.nt_cards = convert_to_args_n(nonterminals)

        self.root = edges[0][0]

        if values is not None:
            self.nodes = {x:Node(x, value=values[x]) for x in self.node_ids}
        else:
            self.nodes = {x:Node(x) for x in self.node_ids}


    def __str__(self):
        stack = []

        for token in reversed(flat_dfs(self.hash_map, self.root)):

            current_node = self.nodes[token]

            if current_node.value not in self.nt_cards:
                stack.append(current_node.value)
            else:
                n_arguments = self.nt_cards[current_node.value]
                operands = [stack.pop() for _ in range(0, n_arguments)]
                stack.append('{}({})'.format(current_node.value, ','.join(operands)))
        
        return stack.pop()
    
    def __call__(self, env=None):
        if env is None:
            env = {}
        return eval(str(self), {**self.nonterminals, **env})

    def copy(self):
        return deepcopy(self)