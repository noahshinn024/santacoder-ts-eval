from typing import List, Dict, Tuple

def Split(list: List[int]) -> List[int]:
    """
	Write a python function which takes a list of integers and only returns the odd ones.
	"""
    ### Canonical solution below ###
    pass

### Unit tests below ###
def check(candidate):
    assert candidate([1, 2, 3, 4, 5, 6]) == [1, 3, 5]
    assert candidate([10, 11, 12, 13]) == [11, 13]
    assert candidate([7, 8, 9, 1]) == [7, 9, 1]

def test_check():
    check(Split)

