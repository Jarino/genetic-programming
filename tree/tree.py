from inspect import signature as sg
from copy import deepcopy


from randomdict import RandomDict

from tree.edges_parser import parse
from tree.search import flat_dfs
from tree.node import Node

from utils.dictionary import convert_to_args_n

class Tree():

    def __init__(self, edges, environment, values=None):
        self.edges = edges
        self.node_ids, self.hash_map = parse(edges)
        self.environment = environment
        self.values = values
        self.root = edges[0][0]

        if values is not None:
            self.nodes = {x:Node(x, value=values[x]) for x in self.node_ids}
        else:
            self.nodes = {x:Node(x) for x in self.node_ids}


    def __str__(self):
        stack = []

        for token in reversed(flat_dfs(self.hash_map, self.root)):

            current_node = self.nodes[token]

            if current_node.value not in self.environment.n_args:
                stack.append(current_node.value)
            else:
                n_arguments = self.environment.n_args[current_node.value]
                operands = [stack.pop() for _ in range(0, n_arguments)]
                stack.append('{}({})'.format(current_node.value, ','.join(operands)))
        
        return stack.pop()
    
    def __call__(self, env=None):
        if env is None:
            env = {}
        return eval(str(self), {**self.environment.nonterminals, **env})

    def copy(self):
        return deepcopy(self)

    def subtree(self, start_node):
        stack = [start_node]
        edges = []
        values = {}

        while len(stack) != 0:
            current_node = stack.pop()

            values[current_node] = self.nodes[current_node].value

            for child_id in self.hash_map[current_node]:
                edges.append((current_node, child_id))
                values[child_id] = self.nodes[child_id].value

            stack += self.hash_map[current_node]

        return edges, values

    def remap(self, start_id=0):
        id_map = { k:v for k,v in zip(self.node_ids, range(start_id, start_id + len(self.node_ids)))}

        self.node_ids = list(range(start_id, start_id + len(self.node_ids)))

        stack = [self.root]
        self.root = start_id
        edges = []
        values = {}
        while len(stack) != 0:
            current_id = stack.pop()
            # add current visited value
            values[id_map[current_id]] = self.nodes[current_id].value
            
            # add children to stack
            stack += self.hash_map[current_id]
            
            # add edges from current node
            for child_id in self.hash_map[current_id]:
                edges.append((id_map[current_id], id_map[child_id]))
            
        self.node_ids, self.hash_map = parse(edges)

        self.nodes = {x:Node(x, value=values[x]) for x in self.node_ids}
            
