from utils.dictionary import reverse
from utils.dictionary import convert_to_args_n

def test_reverse_dictionary():
    original = {
        'a': 1,
        'b': 1,
        'c': 2
    }

    rev = reverse(original)

    assert rev == {1: ['a', 'b'], 2: ['c']} or rev == {1: ['b', 'a'], 2: ['c']}

def test_obtaining_number_of_parameters():
    args_n = convert_to_args_n({
        'sum': lambda x,y,z: x + y + z,
        'diff': lambda x,y: x - y,
        'log': lambda x: x
    })

    assert args_n == {
        'sum': 3,
        'diff': 2,
        'log': 1
    }