from typing import List, Dict, Tuple

def find_min_diff(arr: List[int], n: int) -> int:
    """
	Write a python function to find the minimum difference between any two elements in a given array. https://www.geeksforgeeks.org/find-minimum-difference-pair/
	"""
    ### Canonical solution below ###
    pass

### Unit tests below ###
def check(candidate):
    assert candidate([1, 5, 3, 19, 18, 25], 6) == 1
    assert candidate([4, 3, 2, 6], 4) == 1
    assert candidate([30, 5, 20, 9], 4) == 4

def test_check():
    check(find_min_diff)

