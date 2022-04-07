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

import fi_package


@pytest.mark.xfail(reason='Where we are going...')
def test_something_produces_a_premium_range():
    # GIVEN the state, employee count, and location count
    state = 'VA'
    employees = 70
    locations = 3

    # WHEN data is fed into our process
    result = fi_package.get_indication(state, employees, locations)

    # THEN the result is
    assert result == (100, 500)


@pytest.mark.parametrize(
    'state, expected', [
        pytest.param('VA', 1.0, id='VA is base rate'),
        pytest.param('PA', 2.0, id='PA is twice base rate'),
    ]
)
def test_state_changes_base_rate(state, expected):
    # Given a state
    # When retrieving the rate
    rate = fi_package.get_state_rate(state)
    # Then the result is expected
    assert rate == expected


@pytest.mark.parametrize(
    'rate, base_premium, employee_count, location_count, expected', [
        (1.0, 300, 23, 2, 325),
        pytest.param(2.0, 300, 23, 2, 650, id='Higher rate'),
    ]
)
def test_something_is_base_times_premium_times_state(
    rate, base_premium, employee_count, location_count, expected
):
    # Given a rate, base premium, employee count and location count
    # When the thing is calculated
    result = fi_package.thing_calculator(
        rate, base_premium, employee_count, location_count
    )
    # Then the result is expected
    assert result == expected
