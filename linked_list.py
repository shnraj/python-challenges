class LinkedList():

    # Instantiate LinkedList with no nodes
    def __init__(self, head=None):
        self.head = head

    def get_head(self):
        return self.head

    # Add new nodes to the beginning of the LinkedList
    def add_node(self, value):
        new_node = LinkedListNode(value)
        new_node.next_node = self.head
        self.head = new_node
        return self.head

    def add_nodes_with_array_of_values(self, values_array):
        for value in values_array:
            self.add_node(value=value)

    def size(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next_node
        return count

    def search(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return current_node
            else:
                current_node = current_node.next_node
        return None

    def delete(self, value):
        current_node = self.head
        prev_node = None
        while current_node is not None:
            if current_node.value == value:
                self.remove_node(node=current_node, prev_node=prev_node)
            prev_node = current_node
            current_node = current_node.next_node

    def delete_node(self, node):
        current_node = self.head
        prev_node = None
        while current_node is not None:
            if current_node == node:
                self.remove_node(node=current_node, prev_node=prev_node)
            prev_node = current_node
            current_node = current_node.next_node

    def remove_node(self, node, prev_node):
        if prev_node is None:
            self.head = node.next_node
        else:
            prev_node.next_node = node.next_node

    def remove_dups(self):
        current_node = self.head
        seen_values = set()
        prev_node = None
        while current_node is not None:
            if current_node.value in seen_values:
                self.remove_node(node=current_node, prev_node=prev_node)
            else:
                seen_values.add(current_node.value)
                prev_node = current_node
            current_node = current_node.next_node

    def get_all_data(self):
        current_node = self.head
        values = []
        while current_node is not None:
            values.append(current_node.value)
            current_node = current_node.next_node
        return values


class LinkedListNode():

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
