from typing import List, Dict, Tuple

def differ_At_One_Bit_Pos(a: int, b: int) -> bool:
    """
	Write a python function to check whether the two numbers differ at one bit position only or not.
	"""
    ### Canonical solution below ###
    pass

### Unit tests below ###
def check(candidate):
    assert candidate(13, 9) == True
    assert candidate(15, 8) == False
    assert candidate(2, 4) == False
    assert candidate(2, 3) == True
    assert candidate(5, 1) == True
    assert candidate(1, 5) == True

def test_check():
    check(differ_At_One_Bit_Pos)

