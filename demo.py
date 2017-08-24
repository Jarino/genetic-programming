from rtree.random_tree_factory import RandomTreeFactory
from genetics.operators import point_mutation
from genetics.operators import crossover

factory = RandomTreeFactory()
env = factory.environment
root_node = factory.create()
root_node_b = factory.create()

print('Original a')
print(root_node, root_node(env({
    'x': 10,
    'y': 5
})))

print('Original b')
print(root_node_b, root_node_b(env({
    'x': 10,
    'y': 5
})))

child_a, child_b = crossover(root_node, root_node_b)
print('Child a')
print(child_a, child_a(env({
    'x': 10,
    'y': 5
})))


print('Child b')
print(child_b, child_b(env({
    'x': 10,
    'y': 5
})))


# factory = RandomTreeFactory(5, 2, nonterminals, terminals)

# tree = factory.create()

# try:
#     print(tree, tree({'x': 100, 'y': 12}))
# except ValueError:
#     print('Math domain error')
#     print(tree)
