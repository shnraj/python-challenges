import unittest
from concepts import makeClosure
from concepts import power
from functools import partial


class TestConcepts(unittest.TestCase):

    def test_closure(self):
        clo5 = makeClosure(5)
        clo10 = makeClosure(10)

        self.assertEqual(clo5(2), 7)
        self.assertEqual(clo10(2), 12)

    def test_partial(self):
        square = partial(power, exponent=2)
        cube = partial(power, exponent=3)

        self.assertEqual(square(2), 4)
        self.assertEqual(cube(2), 8)


if __name__ == '__main__':
    unittest.main()
