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
        while current_node:
            count += 1
            current_node = current_node.get_next()
        return count

    def search(self, value):
        current_node = self.head
        while current_node:
            if current_node.get_value() == value:
                return current_node
            else:
                current_node = current_node.get_next()
        return None

    def delete(self, value):
        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.get_value() == value:
                if prev_node is None:
                    self.head = current_node.get_next()
                else:
                    prev_node.set_next(current_node.get_next())
            prev_node = current_node
            current_node = current_node.get_next()

    def remove_dups(self):
        current_node = self.head
        seen_values = []
        while current_node:
            if current_node.get_value() in seen_values:
                self.delete(value=current_node.get_value())
            else:
                seen_values.append(current_node.get_value())
            current_node = current_node.get_next()

    def array_print(self):
        current_node = self.head
        values = []
        while current_node:
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
