import pytest
from msb_priority_reduction import msb_priority_reduction

def test_readme_example():
    seq = msb_priority_reduction([3,2,1,1])
    assert seq[0] == (3,2,1,1)
    assert seq[-1] == (0,0,0,0)
    assert len(seq)-1 == 7

def test_zero_vector():
    seq = msb_priority_reduction([0,0,0])
    assert seq == [(0,0,0)]

def test_empty_vector():
    seq = msb_priority_reduction([])
    assert seq == [()]

@pytest.mark.parametrize("vec", [[1,0,0],[0,2,0],[2,2],[4]])
def test_step_count_equals_sum(vec):
    seq = msb_priority_reduction(list(vec))
    assert len(seq)-1 == sum(vec)

def test_invalid_input_nonint():
    with pytest.raises(ValueError):
        msb_priority_reduction([1, 2.5, 0])

def test_invalid_input_negative():
    with pytest.raises(ValueError):
        msb_priority_reduction([1, -1, 0])
