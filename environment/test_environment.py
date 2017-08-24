from environment.environment import BasicEnvironment

def test_basic_environment_creation():
    be = BasicEnvironment()

    assert sorted(be.symbols_inv[2]) == sorted(['_sum', '_diff'])
    assert be.symbols_inv[1] == ['_sin']
    assert sorted(be.symbols_inv[0]) == sorted(['_int', '_var'])

def test_basic_environment_call():
    be = BasicEnvironment()

    symbols = be({'x': 5, 'y': 10})

    assert symbols['x'] == 5
    assert symbols['y'] == 10
