from tree.tree import Tree
from environment.environment import BasicEnvironment
from environment.environment import Environment

def test_to_string():
    """
    Test the conversion of tree into evaluatable string
    """
    edges = [(1, 2), (2, 4), (2, 5), (1, 3), (3, 6)]

    environment = BasicEnvironment()

    values = {
        1: '_sum',
        2: '_diff',
        3: '_log',
        4: '6',
        5: '4',
        6: '0.5'
    }

    tree = Tree(edges, environment, values=values)
    
    expression = str(tree)

    assert expression == '_sum(_diff(6,4),_log(0.5))'

    edges = [(1, 2), (2, 3), (2, 5), (3, 4)]
    values = {
        1: '_log',
        2: '_sum',
        3: '_log',
        4: '5',
        5: '7'
    }
    
    tree = Tree(edges, environment, values=values)

    expression = str(tree)

    assert expression == '_log(_sum(_log(5),7))'


def test_eval():
    edges = [(1, 2), (1, 3)]
    values = {1: '_sum', 2: 'x1', 3: '7'}
    environment = Environment({
        '_sum': lambda x, y: x + y
    }, ['x1', '7'])

    tree = Tree(edges, environment, values)

    result = tree({'x1': 3})

    assert result == 10

def test_eval_without_variables():
    edges = [(1, 2), (1, 3)]
    values = {1: '_sum', 2: '1', 3: '1'}
    environment = Environment({
        '_sum': lambda x, y: x + y
    }, [])

    tree = Tree(edges, environment, values)
    result = tree()

    assert result == 2

