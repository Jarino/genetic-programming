def test_node_to_string(tree_with_vars):
    nonterminals = {'_sum', '_diff'}

    expression = tree_with_vars.to_expression(nonterminals)

    assert expression == '_sum(_diff(x,z),y)'

def test_node_eval(tree_with_vars):

    nonterminals = {
        '_sum': lambda x, y: x + y,
        '_diff': lambda x, y: x - y
    }

    terminals = {'x': 5, 'y': 3, 'z': 7}

    assert tree_with_vars(nonterminals, terminals) == 1

def test_node_eval_with_number(tree_with_vars_and_numbers):
    nonterminals = {
        '_sum': lambda x, y: x + y,
        '_diff': lambda x, y: x - y
    }

    terminals = {'x': 5, 'z': 7}

    assert tree_with_vars_and_numbers(nonterminals, terminals) == 7

    