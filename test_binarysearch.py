
from pytest import raises
from binsearch import binary_search

def test_binary_search():
    input = list(range(10))
    assert binary_search(input, 5) == 5