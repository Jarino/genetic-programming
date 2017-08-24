from environment.environment import BasicEnvironment

def test_basic_environment_creation():
    be = BasicEnvironment()

    assert sorted(be.symbols_inv[2]) == sorted(['_sum', '_diff'])
    assert be.symbols_inv[1] == ['_log']
    assert sorted(be.symbols_inv[0]) == sorted(['_int', '_var'])
