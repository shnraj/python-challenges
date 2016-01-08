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

    def size(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.get_next()
        return count

    def search(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.get_value() == value:
                return current_node
            else:
                current_node = current_node.get_next()
        return None

    def delete(self, value):
        current_node = self.head
        prev_node = None
        while current_node is not None:
            if current_node.get_value() == value:
                self.remove_node(node=current_node, prev_node=prev_node)
            prev_node = current_node
            current_node = current_node.get_next()

    def remove_node(self, node, prev_node):
        if prev_node is None:
            self.head = node.get_next()
        else:
            prev_node.set_next(node.get_next())

    def remove_dups(self):
        current_node = self.head
        seen_values = set()
        prev_node = None
        while current_node is not None:
            if current_node.get_value() in seen_values:
                self.remove_node(node=current_node, prev_node=prev_node)
            else:
                seen_values.add(current_node.get_value())
                prev_node = current_node
            current_node = current_node.get_next()

    def get_all_data(self):
        current_node = self.head
        values = []
        while current_node is not None:
            values.append(current_node.get_value())
            current_node = current_node.get_next()
        return values


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
