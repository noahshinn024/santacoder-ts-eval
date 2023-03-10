from typing import List, Dict, Tuple

def substract_elements(test_tup1: Tuple[int, int, int], test_tup2: Tuple[int, int, int]) -> Tuple[int, int, int]:
    """
	Write a function that takes in two tuples and subtracts the elements of the first tuple by the elements of the second tuple with the same index.
	"""
    ### Canonical solution below ###
    pass

### Unit tests below ###
def check(candidate):
    assert candidate((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
    assert candidate((11, 2, 3), (24, 45, 16)) == (-13, -43, -13)
    assert candidate((7, 18, 9), (10, 11, 12)) == (-3, 7, -3)

def test_check():
    check(substract_elements)

