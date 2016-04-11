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


# 2D ARRAY
# There aren't multidimensional arrays as such in Python,
# what you have is a list containing other lists.
def create_2d_array_board(size):
    board = [[False for x in range(size)] for y in range(size)]
    # board = [[False, False, False],
    #          [False, False, False],
    #          [False, False, False]] if size = 3

    board[0][0] = True

    for row in board:
        print ' '.join(str(value) for value in row)


# TUPLE
# A tuple consists of a number of values separated by commas
# Tuple is immutable whereas a list is mutable
# You can't add/remove elements from a tuple
# You can use the in operator to check if an element exists in the tuple
# Tuples are faster than lists
# Code safer if you “write-protect” data that does not need to be changed
def tuple():
    t = 123, 234, 'hi'
    # (123, 234, 'hi')
    t[0]  # 123
    t[0] = 4  # not possible
    # TypeError: 'tuple' object does not support item assignment

    u = (1, 2, 3, 4, 5)
    max(u)  # 5
    x = t + u
    # ((123, 234, 'hi'), (1, 2, 3, 4, 5))
    min(x)  # (1, 2, 3, 4, 5)


# SET
# Does not keep duplicates
# Frozen set in immutable (cannot .add or .remove anything)
def set():
    x = set("hi sahana")
    x  # {'h', 'i', ' ', 's', 'a', 'n'}
    y = set('hi', 'sahana')
    y  # {'hi', 'sahana'}

    # x.union(y, ...) Return a new set with elements from the set and all others
    # x.intersection(y, ...) Return a new set with elements common to the set and all others
    # x.difference(y, ...) Return a new set with elements in the set that are not in the others
    # x.symmetric_difference(y) Return a new set with elements in either the set or other but not both
    # x.issubset(y)
    # x.issuperset(y)
    # x.copy() Makes a shallow copy of x

