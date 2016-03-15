# Python concept examples


# CLOSURES

# Nested functions that
# 1) access variables that are local to enclosing scopes,
# 2) do so when they are executed outside of that scope.
def makeClosure(x):
    def clo(y):
        # x is "closed" in the definition of clo
        return y + x
    return clo


# PARTIALS

# Makes versions of a function with one or more arguments already filled in
# The new version of a function documents itself

from functools import partial


def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

# instead of:

# def square(base):
#   return power(base, 2)

# def cube(base):
#   return power(base, 3)
