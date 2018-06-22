from functools import wraps
# Function that wraps other functions that
# changes or enhances their behavior


def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper


# no sugar way
def greet():
    print("My name is April.")


greet = be_polite(greet)
greet()


# lots of sugar way
@be_polite
def greet():
    print("My name is April")


greet()


# decorators with arguments
def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, *kwargs).upper()
    return wrapper


@shout
def greet(name):
    return f"Hi, I'm {name}"


@shout
def order(main, side):
    return f"Hi, I'd like the {manin}, with a side of {side}, please."


# maintaining documentation
def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I am a wrapper function"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x, y):
    """Adds two numbers together."""
    return x + y


# prints the proper docs as they are being printed from
# inside wrapper()
add(10, 2)


# Without @wraps on the wrapper function in log_function_data()
# this will return the wrapper docs, not the add() docs.
print(add.__doc__)
print(add.__name__)
help(add)
