import gc

class Node:
    def __init__(self, value):
        self.next = None
        self.previous = None
        self.value = value


class DLList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, value):
        node = Node(value)
        node.next = self.head

        if self.head:
            self.head = node
            self.head.previous = node
            return node
        else:
            self.head = self.tail = node
            return node

    def push_back(self, value):
        node = Node(value)
        node.previous = self.tail

        if not self.tail:
            self.head = node
            self.tail = node
            return node
        else:
            self.tail.next = node
            self.tail = node
            return node

    def pop_front(self):
        if not self.head:
            return
        else:
            node = self.head
            node.next.previous = None
            self.head = node.next
            node.next = None
            gc.collect()
            return node.value

    def pop_back(self):
        if not self.tail:
            return
        else:
            node = self.tail
            node.previous.next = None
            self.tail = node.previous
            node.previous = None
            gc.collect()
            return node.value

    def pop_node(self, node):
        if not node.previous:
            self.head = node.next
            self.head.previous = None
        elif not node.next:
            self.tail = node.previous
            self.tail.next = None
        else:
            node.previous.next = node.next
            node.next.previous = node.previous
        gc.collect()

    def traverse(self):
        tmp = self.head
        res = []
        while tmp:
            res.append(tmp.value)
            tmp = tmp.next
        return res
