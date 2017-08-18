from tree.tree import Tree
from tree.random import get_random_tree


class RandomTreeFactory():

    def __init__(self, n_nodes, child_limit, nonterminals, terminals):
        self.n_nodes = n_nodes
        self.child_limit = child_limit
        self.nonterminals = nonterminals
        self.terminals = terminals



    def create(self):
        nodes, edges = get_random_tree(self.n_nodes, self.child_limit)


