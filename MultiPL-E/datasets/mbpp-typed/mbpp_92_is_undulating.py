from typing import List, Dict, Tuple

def is_undulating(n: int) -> bool:
    """
	Write a function to check whether the given number is undulating or not.
	"""
    ### Canonical solution below ###
    pass

### Unit tests below ###
def check(candidate):
    assert candidate(1212121) == True
    assert candidate(1991) == False
    assert candidate(121) == True

def test_check():
    check(is_undulating)

