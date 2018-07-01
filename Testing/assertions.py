# Old school
# Can be overridden with a flag when the file is run.


def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive."
    return x + y


add_positive_numbers(1, 1)  # 2
add_positive_numbers(1, -1)  # AssertionError: Both numbers must be positive
