from inspect import signature as sg
from copy import deepcopy


from randomdict import RandomDict

from tree.edges_parser import parse
from tree.search import flat_dfs
from tree.node import Node

from utils.dictionary import convert_to_args_n

class Tree():

    def __init__(self, edges, environment, values=None):
        self.node_ids, self.hash_map = parse(edges)
        self.environment = environment

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
        subtree_map = {}
        while len(stack) != 0:
            current_node = stack.pop()
            subtree_map[current_node] = self.hash_map[current_node][:]
            stack += self.hash_map[current_node]
        
        return subtree_map

    def remap(self, start_id=0):
        new_ids = list(range(start_id, start_id + len(self.node_ids)))
        self.node_ids = new_ids[:]

        stack = [self.root]
        self.root = start_id
        edges = []
        values = {}
        while len(new_ids) != 0:           
            current_id = stack.pop()
            current_node = self.nodes[current_id]

            stack += self.hash_map[current_id]
            
            new_current_id = new_ids.pop(0)
            values[new_current_id] = current_node.value
            
            for child_id in self.hash_map[current_id]:
                new_child_id = new_ids.pop(0)
                values[new_child_id] = self.nodes[child_id].value
                edges.append((new_current_id, new_child_id))
            
        self.node_ids, self.hash_map = parse(edges)

        self.nodes = {x:Node(x, value=values[x]) for x in self.node_ids}
            
