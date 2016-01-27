import unittest
from stack_queue import Stack
from stack_queue import Queue


class TestStack(unittest.TestCase):

    def test_push_and_pop(self):
        stack = Stack()
        stack.push(data=2)
        self.assertEqual(stack.print_stack(), [2])

        stack.push(data=4)
        self.assertEqual(stack.print_stack(), [4, 2])

        stack.pop()
        self.assertEqual(stack.print_stack(), [2])


class TestQueue(unittest.TestCase):

    def test_push_and_pop(self):
        queue = Queue()
        queue.pop()
        self.assertEqual(queue.print_queue(), [])

        queue.push(data=2)
        self.assertEqual(queue.print_queue(), [2])

        queue.push(data=4)
        self.assertEqual(queue.print_queue(), [4, 2])

        queue.pop()
        self.assertEqual(queue.print_queue(), [4])

if __name__ == '__main__':
    unittest.main()
