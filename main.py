class Node:
    def __init__(self, value=None, next_node=None, previous_node=None):
        self.value = value
        self.next = next_node
        self.previous = previous_node

    def set(self, value):
        self.value = value
        return self

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def set_next(self, next_node):
        self.next = next_node
        return self

    def set_previous(self, previous_node):
        self.previous = previous_node
        return self


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  # To keep track of the number of nodes in the list

    def is_empty(self):
        return self.size == 0

    def add_to_end(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            new_node.set_previous(self.tail)
            self.tail = new_node
        self.size += 1

    def remove_at_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        if index == 0:  # Removing the head node
            self.remove_first()
        elif index == self.size - 1:  # Removing the tail node
            self.remove_last()
        else:
            current = self.head
            for _ in range(index):
                current = current.get_next()

            prev_node = current.get_previous()
            next_node = current.get_next()

            if prev_node:
                prev_node.set_next(next_node)
            if next_node:
                next_node.set_previous(prev_node)

            self.size -= 1

    def get_at_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        current = self.head
        for _ in range(index):
            current = current.get_next()

        return current.get_value()

    def get_first(self):
        if self.is_empty():
            return None
        return self.head.get_value()

    def get_last(self):
        if self.is_empty():
            return None
        return self.tail.get_value()

    def reverse(self):
        current = self.head
        while current:
            # Swap next and previous
            current.set_next(current.get_previous())
            current.set_previous(current.get_next())
            current = current.get_previous()  # Move to the next node (which is previous originally)
        
        # Swap head and tail
        self.head, self.tail = self.tail, self.head

    def remove_first(self):
        if self.is_empty():
            return None
        if self.head == self.tail:  # Only one element in the list
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()
            self.head.set_previous(None)
        self.size -= 1

    def remove_last(self):
        if self.is_empty():
            return None
        if self.head == self.tail:  # Only one element in the list
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.get_previous()
            self.tail.set_next(None)
        self.size -= 1

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.get_value()))
            current = current.get_next()
        return " <-> ".join(values)


# Testing the LinkedList class
ll = LinkedList()
ll.add_to_end(10)
ll.add_to_end(20)
ll.add_to_end(30)
ll.add_to_end(40)

print("Initial list:", ll)
print("First element:", ll.get_first())
print("Last element:", ll.get_last())

print("Element at index 2:", ll.get_at_index(2))

# Remove element at index 2 (value 30)
ll.remove_at_index(2)
print("List after removal at index 2:", ll)

# Check if list is empty
print("Is the list empty?", ll.is_empty())

# Reverse the list
ll.reverse()
print("Reversed list:", ll)

# Remove the first and last elements
ll.remove_first()
ll.remove_last()
print("List after removing first and last:", ll)