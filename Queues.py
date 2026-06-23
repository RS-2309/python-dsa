class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __repr__(self): #O(n)
        if self.size == 0:
            return '[]'
        queue = f'[{self.head.value}'
        current = self.head.next
        while current:
            queue += f', {current.value}'
            current = current.next
        queue += ']'
        return queue

    def __contains__(self, value): #O(n)
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __len__(self): #O(1)
        return self.size

    def enqueue(self, value): #O(1)
        if self.size == 0:
            new = QueueNode(value)
            self.head = new
            self.tail = new
            self.size += 1
        else:
            new = QueueNode(value)
            self.tail.next = new
            self.tail = new
            self.size += 1

    def dequeue(self): #O(1)
        if self.size == 0:
            raise IndexError("Dequeue from empty queue")
        
        elif self.size == 1:
            deleted_value = self.head.value
            self.head = None
            self.tail = None
            self.size = 0
            return deleted_value

        else:
            deleted_node = self.head
            self.head = self.head.next
            deleted_node.next = None
            self.size -= 1
            return deleted_node.value

    def peek(self): #O(1)
        if self.size == 0:
            raise IndexError("Peek from empty queue")
        return self.head.value

    def is_empty(self): #O(1)
        return self.size == 0

    def clear(self): #O(1)
        self.head = None
        self.tail = None
        self.size = 0