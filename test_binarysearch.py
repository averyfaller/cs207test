
from pytest import raises
from binsearch import binary_search

def test_binary_search():
    input = list(range(10))
    assert binary_search(input, 5) == 5
    
def test_empty_array():
    assert binary_search([], 4) == Null

def test_binary_too_big():
    assert binary_search([2, 3], 4) == Null
    
def test_binary_too_small():
    assert binary_search([2, 3], 1) == Null
    
def test_binary_NaN():
    assert binary_search([2, 3, 'a'], 1) == Null
    
def test_middle_needle():
    assert binary_search([2, 4], 3) == Null
    
def test_small():
    assert binary_search([2, 3, 4, 5], 2) == Null
    
def test_big():
    assert binary_search([2, 3, 4, 5], 5) == Null