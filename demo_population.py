from rtree.random_tree_factory import RandomTreeFactory

factory = RandomTreeFactory()
env = factory.environment

population = [
    factory.create() for _ in range(0,100)
]
