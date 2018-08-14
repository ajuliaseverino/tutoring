import pytest
from tut import basics


def test_first():
    a = basics.pos_neg(8)
    assert a == 10
    print("got back {}".format(a))
    y = basics.pos_neg(-1)
    assert y == -3
    print("got back {}".format(y))
    b = basics.pos_neg(0)
    assert b == 2
    with pytest.raises(TypeError):
        basics.pos_neg("things")


def test_simple_calc():
    a = basics.simple_calculator(2, "+", 3)
    assert a == 5

