from unittest.mock import Mock
from unittest.mock import patch

from rtree.random_tree_factory import RandomTreeFactory



@patch('utils.random.choice')
def test_random_creation(choice_mock):
    choice_mock.side_effect = lambda x: x[0]

    env = Mock(symbols={
        '_sum': lambda x, y: x + y,
        '_var': lambda: 'x'  
    }, symbols_inv={
        2: ['_sum'],
        0: ['_var']
    })

    factory = RandomTreeFactory(max_depth=3, environment=env)

    assert set(factory.arities) == set([0, 2])

    # fix the arities, so choice_mock wont choose the zero arity
    factory.arities = [2] 
    tree = factory.create()

    assert str(tree) == '_sum(_sum(x,x),_sum(x,x))'
    