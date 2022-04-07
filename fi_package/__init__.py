def get_state_rate(state: str) -> float:
    if state == 'PA':
        return 2.0
    return 1.0


def get_indication(state, employees, locations):
    return None


def calculate():
    rate = base_premium = employee_count = location_count = 0
    return sum([
        rate * base_premium,
        rate * employee_count,
        rate * location_count
    ])


def thing_calculator(rate, base_premium, employee_count, location_count):
    return sum([
        rate * base_premium,
        rate * employee_count,
        rate * location_count
    ])