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


# COUNTER (TO TALLY)
# Use as a non-unique set
from collections import Counter


def count_list():
    cnt = Counter('sahana')  # Counter({'a': 3, 'h': 1, 's': 1, 'n': 1})
    cnt2 = Counter(['sahana', 'raj'])  # Counter({'sahana': 1, 'raj': 1})

    # Create a list of elements from the Counter object
    list(cnt.elements())  # ['a', 'a', 'a', 'h', 's', 'n']
    list(cnt2.elements())  # ['sahana', 'raj']

    # Counter has 'most_common' that allows you to sort items by their count
    cnt.most_common(2)  # [('a', 3), ('h', 1)]

    c = Counter(a=3, b=1)
    d = Counter(a=1, b=2)


    c + d                       # add two counters together:  c[x] + d[x]
    # Counter({'a': 4, 'b': 3})
    c - d                       # subtract (keeping only positive counts)
    # Counter({'a': 2})
    c & d                       # intersection:  min(c[x], d[x])
    # Counter({'a': 1, 'b': 1})
    c | d                       # union:  max(c[x], d[x])
    # Counter({'a': 3, 'b': 2})


