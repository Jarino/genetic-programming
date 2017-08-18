from utils.dictionary import reverse


def test_reverse_dictionary():
    original = {
        'a': 1,
        'b': 1,
        'c': 2
    }

    rev = reverse(original)

    assert rev == {1: ['a', 'b'], 2: ['c']} or rev == {1: ['b', 'a'], 2: ['c']}