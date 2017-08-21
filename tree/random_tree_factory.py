from tree.tree import Tree
from tree.random import get_random_tree
from tree.random import assign_random_symbols

from utils.dictionary import convert_to_args_n

class RandomTreeFactory():

    def __init__(self, n_nodes, child_limit, nonterminals, terminals):
        self.n_nodes = n_nodes
        self.child_limit = child_limit
        self.nonterminals = nonterminals
        self.terminals = terminals

    def create(self):
        """
        Returns random tree with number of nodes, nonterminal and terminal
        symbols defined in the factory
        """
        _, edges = get_random_tree(self.n_nodes, self.child_limit)
        args_n = convert_to_args_n(self.nonterminals)
        values = assign_random_symbols(edges, args_n, self.terminals)
        return Tree(edges, self.nonterminals, values)



