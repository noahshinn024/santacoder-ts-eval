from typing import List, Dict, Tuple

def noprofit_noloss(actual_cost: int, sale_amount: int) -> bool:
    """
	Write a function to check whether the given amount has no profit and no loss
	"""
    ### Canonical solution below ###
    pass

### Unit tests below ###
def check(candidate):
    assert candidate(1500, 1200) == False
    assert candidate(100, 100) == True
    assert candidate(2000, 5000) == False

def test_check():
    check(noprofit_noloss)

