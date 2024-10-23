import pytest
import random

@pytest.fixture
def nums_random():
    return random.randint(0,100)

@pytest.fixture
def plus(nums_random):
    return nums_random + nums_random

def test_nums_random(plus):
    assert plus % 2 == 0