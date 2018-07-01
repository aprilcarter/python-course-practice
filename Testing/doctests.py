# Here for completeness. Other doc tools will serve better


# Write doctests in doc strings
def add(x, y):
    """add together x and y

    >>> add(1, 2) ##Doing this
    3 ##Should get this

    >>> add(8, "hi")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """

# To run tests and output results to console:
#   python3 -m doctest -v file_name.py

# Caveats:
#   --Theoretical results must match exactly the
#     expected output or the test will fail even
#     if the output is correct
#   --Cannot test strings with double quotes. All
#     string results are expected to have single quotes
#   --Extra white space will cause a fail
#   --Dictionary order (which shouldn't be relevant)
#     can cause a fail
