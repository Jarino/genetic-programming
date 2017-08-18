from tree.tree import Tree


def test_to_string():
    """
    Test the conversion of tree into evaluatable string
    """
    edges = [(1, 2), (2, 4), (2, 5), (1, 3), (3, 6)]

    nonterminals = {
        'sum': 2,
        'prod': 2,
        'log': 1,
        'sin': 1
    }

    values = {
        1: 'sum',
        2: 'prod',
        3: 'log',
        4: '6',
        5: '4',
        6: '0.5'
    }

    tree = Tree(edges, nonterminals, values=values)
    
    expression = str(tree)

    assert expression == 'sum(prod(6,4),log(0.5))'

    edges = [(1, 2), (2, 3), (2, 5), (3, 4)]
    values = {
        1: 'log',
        2: 'sum',
        3: 'sin',
        4: '5',
        5: '7'
    }
    
    tree = Tree(edges,nonterminals, values=values)

    expression = str(tree)

    assert expression == 'log(sum(sin(5),7))'


def test_eval():
    edges = [(1, 2), (1, 3)]
    values = {1: '_sum', 2: 'x1', 3: '7'}
    nonterminals = {
        '_sum': 2
    }

    def _sum(*args):
        return sum(args)


    tree = Tree(edges, nonterminals, values)

    expression = str(tree)
    print(expression)
    result = eval(expression, {'x1': 3, '_sum': _sum})

    assert result == 10


