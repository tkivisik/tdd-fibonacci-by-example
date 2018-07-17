 # -*- coding: utf-8 -*-
import pytest

from fibonacci import fibonacci

@pytest.mark.parametrize("test_input,expected",[
        (0,0),
        (1,1),
        (2,1),
        (3,2)])
def test_fibonacci(test_input, expected):
    assert fibonacci(test_input) == expected
