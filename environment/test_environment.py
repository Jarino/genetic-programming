from environment.environment import BasicEnvironment

def test_basic_environment_creation():
    be = BasicEnvironment()

    assert be.n_args == {
        '_log': 1,
        '_sum': 2,
        '_diff': 2
    }

    assert be.reversed_n_args == {
        1: ['_log'],
        2: ['_diff', '_sum']
    } or be.reversed_n_args == {
        1: ['_log'],
        2: ['_sum', '_diff']
    } 