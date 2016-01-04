class LinkedList():

    def __init__(self, value):
        new_node = LinkedListNode(value)
        self.head = new_node
        self.tail = new_node

    def add_node(self, value):
        new_node = LinkedListNode(value)
        self.tail.next = new_node
        self.tail = new_node

    # REMOVE DUPLICATES FROM A LINKED LIST

    # def remove_dups(self):


class LinkedListNode():

    def __init__(self, value=None):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node
