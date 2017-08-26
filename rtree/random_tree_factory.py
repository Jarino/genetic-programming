from random import choice

from environment.environment import BasicEnvironment
from utils.random import get_random_tree
from utils.random import assign_random_symbols
from utils.edges_parser import parse_to_nodes

class RandomTreeFactory():

    def __init__(self, nodes=None, environment=None):
        if environment is None:
            self.environment = BasicEnvironment()
        else:
            self.environment = environment

        if nodes == None:
            self.nodes = list(range(3,6))

        self.max_children = max(self.environment.symbols_inv.keys())

    def create(self):
        _, edges = get_random_tree(
            choice(self.nodes),
            self.max_children
        )

        values = assign_random_symbols(edges, self.environment)

        root_node, _ = parse_to_nodes(edges, values)

        return root_node
