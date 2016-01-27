class Stack():

    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        self.head = StackNode(data=data, next_node=self.head)

    def pop(self):
        node = self.head
        self.head = node.next_node
        return node.data

    def print_stack(self):
        current_node = self.head
        arr = []
        while current_node:
            arr.append(current_node.get_data())
            current_node = current_node.get_next_node()
        return arr


class StackNode():

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node
