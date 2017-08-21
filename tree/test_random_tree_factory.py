from tree.random_tree_factory import RandomTreeFactory


def test_random_tree_factory():
    factory = RandomTreeFactory(3, 2, {
        '_sum': lambda x, y: x + y, 
        '_dummy': lambda x: x + 2
        }, ['2']
    )
    tree = factory.create()
    
    assert tree() == 4 or tree() == 6


    