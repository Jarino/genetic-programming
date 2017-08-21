from math import log

from utils import operators as ops

from tree.random_tree_factory import RandomTreeFactory

nonterminals = {
    'c_sum': lambda x, y: x + y,
    'c_log': lambda x: log(x), 
    'c_diff': lambda x, y: x - y, 
    'c_prod': lambda x, y: x* y
}
terminals = ['x', 'y']

factory = RandomTreeFactory(5, 2, nonterminals, terminals)

tree = factory.create()

try:
    print(tree, tree({'x': 100, 'y': 12}))
except ValueError:
    print('Math domain error')
    print(tree)
