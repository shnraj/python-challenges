class LinkedList():

    # Instantiate LinkedList with no nodes
    def __init__(self, head=None):
        self.head = head

    def get_head(self):
        return self.head

    # Add new nodes to the beginning of the LinkedList
    def add_node(self, value):
        new_node = LinkedListNode(value)
        new_node.set_next(self.head)
        self.head = new_node

    def add_nodes_with_array_of_values(self, values_array):
        for value in values_array:
            self.add_node(value=value)

    # Size of LinkedList
    def size(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.get_next()
        return count

    # Search LinkedList for value
    def search(self, value):
        current_node = self.head
        while current_node:
            if current_node.get_value() == value:
                return current_node
            else:
                current_node = current_node.get_next()
        return None

    # REMOVE DUPLICATES FROM A LINKED LIST

    # def remove_dups(self):


class LinkedListNode():

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node
