# EXPLORE PYTHON BUILT IN FUNCTIONS


def explore():
    # ABS
    assert abs(4/3) == 1

    # ALL
    assert all([1, 2, 3]) is True
    assert all([1, False, 2]) is False
    assert all([]) is True

# EXPLORE PYTHON ITERATOR FUNCTIONS
import itertools


def explore_itertools():
    # CHAIN
    # chain() function takes several iterators as arguments and returns
    # a single iterator that produces the contents of all of them as though
    # they came from a single sequence

    chained = []
    for i in itertools.chain([1, 2, 3], ['a', 'b', 'c']):
        chained.append(i)

    assert chained == [1, 2, 3, 'a', 'b', 'c']
