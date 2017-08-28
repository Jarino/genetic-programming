from environment.environment import BasicEnvironment
from utils.random import get_random_tree
from utils.random import assign_random_symbols
from utils.edges_parser import parse_to_nodes

class RandomTreeFactory():

    def __init__(self, max_depth=None, environment=None):

        self.environment = BasicEnvironment if environment is None else environment

        self.max_depth = 3 if max_depth is None else max_depth

        self.arities = list(self.environment.symbols_inv.keys())

    def create(self):
        _, edges = get_random_tree(self.max_depth, self.arities)

        values = assign_random_symbols(edges, self.environment)

        root_node, _ = parse_to_nodes(edges, values)

        return root_node
