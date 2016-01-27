class Stack():

    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        self.head = StackNode(data=data, next=self.head)

    def pop(self):
        node = self.head
        self.head = node.next
        return node.data


class StackNode():

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
