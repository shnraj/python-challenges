import unittest
from linked_list import LinkedList
from linked_list import LinkedListNode


class TestLinkedList(unittest.TestCase):

    def test_init(self):
        ll = LinkedList()
        self.assertTrue(ll.get_head() is None)

        ll_node = LinkedListNode()
        self.assertTrue(ll_node.get_value() is None)
        self.assertTrue(ll_node.get_next() is None)

        ll_node_2 = LinkedListNode(value=2)
        self.assertTrue(ll_node_2.get_value() == 2)
        self.assertTrue(ll_node_2.get_next() is None)

        ll_2 = LinkedList(head=ll_node_2)
        self.assertTrue(ll_2.get_head() is ll_node_2)

        ll_node_3 = LinkedListNode(value=2, next_node=ll_node_2)
        self.assertTrue(ll_node_3.get_value() == 2)
        self.assertTrue(ll_node_3.get_next() == ll_node_2)

    def test_add_node(self):
        ll = LinkedList()
        ll.add_node(value=1)
        self.assertTrue(ll.get_head() is not None)
        self.assertTrue(ll.get_head().get_value() == 1)

    def test_size(self):
        ll = LinkedList()
        self.assertTrue(ll.size() == 0)

        ll.add_node(value=1)
        self.assertTrue(ll.size() == 1)

        ll.add_node(value=1)
        self.assertTrue(ll.size() == 2)

    def test_search_and_add_nodes_with_array_of_values(self):
        ll = LinkedList()
        ll.add_nodes_with_array_of_values(values_array=[1])
        self.assertTrue(ll.search(value=1) is not None)
        self.assertTrue(ll.search(value=2) is None)

        ll.add_nodes_with_array_of_values(values_array=[2, 3])
        self.assertTrue(ll.search(value=2) is not None)
        self.assertTrue(ll.search(value=3) is not None)

    def test_delete(self):
        ll = LinkedList()
        ll.add_nodes_with_array_of_values(values_array=[1, 2, 3, 2])
        ll.delete(value=2)
        self.assertTrue(ll.search(value=2) is None)
        self.assertTrue(ll.search(value=3) is not None)

    def test_remove_dups(self):
        ll = LinkedList()
        ll.add_nodes_with_array_of_values(values_array=[1, 2, 3, 2])
        ll.remove_dups()
        self.assertTrue(ll.search(value=2) is None)
        self.assertTrue(ll.search(value=3) is not None)


if __name__ == '__main__':
    unittest.main()
