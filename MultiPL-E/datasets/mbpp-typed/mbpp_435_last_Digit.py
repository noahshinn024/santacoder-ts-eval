from typing import List, Dict, Tuple

def last_Digit(n: int) -> int:
    """
	Write a python function to find the last digit of a given number.
	"""
    ### Canonical solution below ###
    pass

### Unit tests below ###
def check(candidate):
    assert candidate(123) == 3
    assert candidate(25) == 5
    assert candidate(30) == 0

def test_check():
    check(last_Digit)

