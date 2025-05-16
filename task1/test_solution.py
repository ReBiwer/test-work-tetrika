import pytest
from task1.solution import strict

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

@strict
def concat(a: str, b: str) -> str:
    return a + b

def test_sum_two_correct():
    assert sum_two(1, 2) == 3

def test_sum_two_type_error():
    with pytest.raises(TypeError):
        sum_two(1, 2.5)

def test_concat_correct():
    assert concat('a', 'b') == 'ab'

def test_concat_type_error():
    with pytest.raises(TypeError):
        concat('a', 2) 