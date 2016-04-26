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


def explore_counter():
    cnt = Counter('sahana')
    assert cnt == Counter({'a': 3, 'h': 1, 's': 1, 'n': 1})
    cnt2 = Counter(['sahana', 'raj'])
    assert cnt2 == Counter({'sahana': 1, 'raj': 1})

    # Create a list of elements from the Counter object
    assert list(cnt.elements()) == ['a', 'a', 'a', 'h', 's', 'n']
    assert list(cnt2.elements()) == ['sahana', 'raj']

    # Counter has 'most_common' that allows you to sort items by their count
    assert cnt.most_common(2) == [('a', 3), ('h', 1)]

    c = Counter(a=3, b=1)
    d = Counter(a=1, b=2)

    assert c + d == Counter({'a': 4, 'b': 3})  # add two counters together:  c[x] + d[x]
    assert c - d == Counter({'a': 2})          # subtract (keeping only positive counts)
    assert c & d == Counter({'a': 1, 'b': 1})  # intersection:  min(c[x], d[x])
    assert c | d == Counter({'a': 3, 'b': 2})  # union:  max(c[x], d[x])


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
# Code safer if you "write-protect" data that does not need to be changed
def explore_tuple():
    t = 123, 234, 'hi'
    assert t == (123, 234, 'hi')
    assert t[0] == 123
    # not possible
    # t[0] = 4
    # TypeError: 'tuple' object does not support item assignment

    u = (1, 2, 3, 4, 5)
    assert max(u) == 5
    x = t + u
    assert x == (123, 234, 'hi', 1, 2, 3, 4, 5)
    assert min(x) == 1


# SET
# Does not keep duplicates
# Frozen set in immutable (cannot .add or .remove anything)
def explore_set():
    x = set("hi sahana")
    assert x == {'h', 'i', ' ', 's', 'a', 'n'}
    y = set(['hi', 'sahana'])
    assert y == {'hi', 'sahana'}

    # x.union(y, ...) Return a new set with elements from the set and all others
    # x.intersection(y, ...) Return a new set with elements common to the set and all others
    # x.difference(y, ...) Return a new set with elements in the set that are not in the others
    # x.symmetric_difference(y) Return a new set with elements in either the set or other but not both
    # x.issubset(y)
    # x.issuperset(y)
    # x.copy() Makes a shallow copy of x


# SORT
def explore_sort():
    simple_list = [3, 4, 2, 1]

    # .sort modifies existing list, only works for lists
    simple_list.sort()
    assert simple_list == [1, 2, 3, 4]

    list = [3, 4, 2, 1]

    # sorted() reates new sorted list
    new_list = sorted(list)
    assert new_list == [1, 2, 3, 4]
    # list does not change
    assert list == [3, 4, 2, 1]

    # Sort a dictionary?
    # It is not possible to sort a dict. Dicts are inherently orderless,
    # but other types, such as lists and tuples, are not. So you need a sorted
    # representation, which will be a list-probably a list of tuples
    new_list = sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
    assert new_list == [1, 2, 3, 4, 5]

    student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
    ]

    new_student_tuples = sorted(student_tuples, key=sort_key)
    assert new_student_tuples == [
        ('dave', 'B', 10),
        ('jane', 'B', 12),
        ('john', 'A', 15),
    ]

    new_list = sorted(list, reverse=True)
    assert new_list == [4, 3, 2, 1]


def sort_key(item):
    return item[2]

# OPERATOR
# Python provides convenience functions to make accessor functions easier and faster.
# The operator module has itemgetter, attrgetter, and starting in Python 2.6 a methodcaller function.

# Each of these returns a function -
# operator.itemgetter(item)
# operator.attrgetter('.attribute')
# operator.methodcaller('method name' or 'list of comma separated method names')
import operator


def explore_operator():
    student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10)
    ]

    assert sorted(student_tuples, key=operator.itemgetter(2)) == [
        ('dave', 'B', 10),
        ('jane', 'B', 12),
        ('john', 'A', 15)
    ]

    class Student:
        def __init__(self, name, grade, age):
            self.name = name
            self.grade = grade
            self.age = age

        def __repr__(self):
            return repr((self.name, self.grade, self.age))

        def weighted_grade(self):
            return 'CBA'.index(self.grade) / float(self.age)

    s1 = Student('john', 'A', 15)
    s2 = Student('jane', 'B', 12)
    s3 = Student('dave', 'B', 10)

    student_objects = [
        s1,
        s2,
        s3
    ]

    assert sorted(student_objects, key=operator.attrgetter('age')) == [s3, s2, s1]

    # Using methodgetter
    sorted(student_objects, key=operator.methodcaller('weighted_grade'))


if __name__ == '__main__':
    explore_counter()
    explore_tuple()
    explore_set()
    explore_sort()
    explore_operator()
