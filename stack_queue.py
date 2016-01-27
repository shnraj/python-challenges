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


class Queue():

    def __init__(self, head=None):
        self.head = head
        self.tail = self.head

    def push(self, data=None):
        new_node = QueueNode(data=data, next_node=self.head, prev_node=None)
        if self.head:
            self.head.prev_node = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def pop(self):
        if self.tail:
            data = self.tail.data
            self.tail.prev_node.next_node = None
            self.tail = self.tail.prev_node
            return data
        return None

    def print_queue(self):
        current_node = self.head
        arr = []
        while current_node:
            arr.append(current_node.data)
            current_node = current_node.next_node
        return arr


class QueueNode():

    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node
