class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_last(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while (current_node.next):
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1

    def show_all_items(self):
        current_node = self.head
        if current_node:
            print(current_node.val)
            while (current_node.next):
                print(current_node.next.val)
                current_node = current_node.next
        else:
            print("Empty")

    def get(self, index):
        current_index = 0
        current_node = self.head
        value_at_index = None
        while (current_node.next):
            if index == current_index:
                value_at_index = current_node.val
                break
            current_index += 1
            current_node = current_node.next
        return value_at_index

    def insert(self, index, value):
        if index < 0 or not value:
            return None
        if index == 0:
            node = Node(value)
            next_node = self.head
            self.head = node
            node.next = next_node
            self.length += 1
            return index
        current_node = self.head
        node_index = 1
        while (current_node.next):
            if index == node_index:
                break
            current_node = current_node.next
            node_index += 1
        if index > node_index:
            return None
        node = Node(value)
        next_node = current_node.next
        current_node.next = node
        node.next = next_node
        self.length += 1
        return index
