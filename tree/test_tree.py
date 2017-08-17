from tree.tree import Tree


def test_to_string():
    """
    Test the conversion of tree into evaluatable string
    """
    tree = Tree([(1, 2), (2, 4), (2, 5), (1, 3), (3, 6)],
                {
                    1: 'sum',
                    2: 'prod',
                    3: 'log',
                    4: '6',
                    5: '4',
                    6: '0.5'
                })
    
    expression = str(tree)

    assert expression == 'sum(prod(6,4),log(0.5))'

    tree = Tree([(1, 2), (2, 3), (2, 5), (3, 4)],
    {
        1: 'log',
        2: 'sum',
        3: 'sin',
        4: '5',
        5: '7'
    })

    expression = str(tree)

    assert expression == 'log(sum(sin(5),7))'


