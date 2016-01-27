import unittest
from stack_queue import Stack


class TestStack(unittest.TestCase):

    def test_push_and_pop(self):
        stack = Stack()
        stack.push(data=2)
        self.assertEqual(stack.print_stack(), [2])

        stack.push(data=4)
        self.assertEqual(stack.print_stack(), [4, 2])

        stack.pop()
        self.assertEqual(stack.print_stack(), [2])


if __name__ == '__main__':
    unittest.main()
