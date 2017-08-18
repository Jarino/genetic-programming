from utils import operators as ops

from tree.random_tree_factory import RandomTreeFactory

nonterminals = {'_sum': 2, '_log': 1, '_diff': 2, '_prod': 2}
terminals = ['x', 'y']

factory = RandomTreeFactory(5, 2, nonterminals, terminals)

tree = factory.create()

try:
    result = eval(str(tree), {
        'x': 5, 'y': 9,
        '_sum': ops.c_sum,
        '_log': ops.c_log, 
        '_diff': ops.c_diff,
        '_prod': ops.c_prod
    })

    print(tree, result)
except ValueError:
    print('Math domain error')
    print(tree)

