from typing import List, Dict, Tuple

def Find_Min_Length(lst: List[List[int]]) -> int:
    """
	Write a python function to find the length of the smallest list in a list of lists.
	"""
    ### Canonical solution below ###
    pass

### Unit tests below ###
def check(candidate):
    assert candidate([[1], [1, 2]]) == 1
    assert candidate([[1, 2], [1, 2, 3], [1, 2, 3, 4]]) == 2
    assert candidate([[3, 3, 3], [4, 4, 4, 4]]) == 3

def test_check():
    check(Find_Min_Length)

