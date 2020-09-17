class Node:
    def __init__(self, value, next_node):
        self.value = value
        selfn next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None
    
    def add_to_head(self, value):
        # Create a new node
        new_node = Node(value)

        if self.head is None:
            # update head & tail attributes
            self.head = new_node
            self.tail = new_node
        else:
            # set the next_node of my new node to the head
            new_node.set_next_node(self.head)
            # update the head attribute
            self.head = new_node

    def add_to_tail(self, value):
        # TODO

    def remove_head(self):
        # cases to consider?
        # empty list
        if self.head = None:
            return None
        # else return value of old list
        else:
            ret_value = self.head.get_value()
            if self.head == self.tail:
                self.head = None
                self.tail = None
            # list with +2 - return value of the old head
            else:
                self.head = self.head.get_next_node()
            return ret_value

    def remove_tail(self):
        # TODO

    def contains(self, value):
        # TODO time permitting

    def get_max(self):
        # TODO time permitting
