from typing import List, Dict, Tuple

def split_Arr(l: List[int], n: int) -> List[int]:
    """
	Write a python function to split a list at the nth eelment and add the first part to the end.
	"""
    ### Canonical solution below ###
    pass

### Unit tests below ###
def check(candidate):
    assert candidate([12, 10, 5, 6, 52, 36], 2) == [5, 6, 52, 36, 12, 10]
    assert candidate([1, 2, 3, 4], 1) == [2, 3, 4, 1]
    assert candidate([0, 1, 2, 3, 4, 5, 6, 7], 3) == [3, 4, 5, 6, 7, 0, 1, 2]

def test_check():
    check(split_Arr)

