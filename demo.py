from math import log
from tree.edges_parser import parse_to_nodes
from utils import operators as ops
from tree.random import get_random_tree
from tree.random import assign_random_symbols
from tree.random_tree_factory import RandomTreeFactory
from utils.dictionary import convert_to_args_n
nonterminals = {
    'c_sum': lambda x, y: x + y,
    'c_log': lambda x: log(x), 
    'c_diff': lambda x, y: x - y, 
    'c_prod': lambda x, y: x* y
}

n_args = convert_to_args_n(nonterminals)

terminals = ['x', 'y']

_, edges = get_random_tree(5,2)
values = assign_random_symbols(edges, n_args, terminals)
root_node, _  = parse_to_nodes(edges, values)


print(root_node)

print(root_node())


# factory = RandomTreeFactory(5, 2, nonterminals, terminals)

# tree = factory.create()

# try:
#     print(tree, tree({'x': 100, 'y': 12}))
# except ValueError:
#     print('Math domain error')
#     print(tree)
