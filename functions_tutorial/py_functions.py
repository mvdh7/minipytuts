def add_and_square(a, b, c=5, d=22):
    """Add inputs and square them."""  # docstring
    added = a + b + c + d
    squared = added ** 2
    return added, squared


x, y = add_and_square(5, 6, d=1)  # only provide values for the kwargs you need
                                  # in whatever order you need them


def subtract(a, b):
    return b - a

# Splatting
a = 5
b = 6
args = [a, b]  # make a list of the args
add, square = add_and_square(*args)  # use * to "splat" them into the function
subt = subtract(*args)

kwargs = {"c": 5, "d": 8}
kwarg = dict(c=5, d=8)  # alternative way to make a dict
add, square = add_and_square(*args, **kwargs)

# Functions vs methods
import numpy as np
data = [1, 2, 3, 4, 5]
data_mean = np.mean(data)  # function
data = np.array(data)
data_mean = data.mean()  # method to do exactly the same as the function


# scope
def times_by_temp(var):
    newvar = 3
    return (temp * var) ** newvar

temp = 15


print(times_by_temp(3))

temp = 10

print(times_by_temp(3))

# print(newvar)  # doesn't work - variable is confined within function


# importance of brackets
def say_hello():
    print("Hi there")
    return 5

x = say_hello()  # x becomes 5 (the output of say_hello)
x = say_hello  # x becomes the function say_hello
