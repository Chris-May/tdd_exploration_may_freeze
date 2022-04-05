"""
What is TDD?
It's sorta:
1. Write a test that shows what you want to do
2. run the test, make sure it fails
3. make the smallest change that affects the result of the test
4. repeat test
5. if passes refactor

Today's task:
    Return a premium indication (range) for a product line
    The low & high end should be 10% below and above the calculated value

Keys:
- base rate is manipulated by state
"""
import pytest

from fi_package import get_indication


def test_something_produces_a_premium_range():
    # GIVEN the state, employee count, and location count
    state = 'VA'
    employees = 70
    locations = 3

    # WHEN data is fed into our process
    result = get_indication(state, employees, locations)

    # THEN the result is
    assert result == (100, 500)


@pytest.mark.parametrize('state, result', [])
def test_state_changes_base_rate():
    # GIVEN the state, employee count, and location count
    state = 'PA'
    employees = 70
    locations = 3

    # WHEN data is fed into our process
    result = get_indication(state, employees, locations)

    # THEN the result is
    assert result == (200, 500)
