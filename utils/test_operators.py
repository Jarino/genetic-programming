from math import log
from math import e

import utils.operators as ops


def test_sum():
    assert ops.c_sum(1,2) == 3
    assert ops.c_sum(5) == 5
    assert ops.c_sum(3,4,5) == 12

def test_log():
    assert ops.c_log(e) == 1
    assert ops.c_log(0) == 0
    assert ops.c_log(-19) == 0

def test_div():
    assert ops.c_div(10,5) == 2
    assert ops.c_div(1,0) == 0
    
