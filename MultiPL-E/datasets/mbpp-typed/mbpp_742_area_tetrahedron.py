from typing import List, Dict, Tuple

def area_tetrahedron(side: int) -> float:
    """
	Write a function to caluclate the area of a tetrahedron.
	"""
    ### Canonical solution below ###
    pass

### Unit tests below ###
def check(candidate):
    assert candidate(3) == 15.588457268119894
    assert candidate(20) == 692.8203230275509
    assert candidate(10) == 173.20508075688772

def test_check():
    check(area_tetrahedron)

