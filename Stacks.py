class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __repr__(self): #O(n)
        if self.size == 0:
            return "[]"
        current = self.head
        stack = f'[{current.value}'
        while current.next:
            current = current.next
            stack += f', {current.value}'
        stack += ']'
        return stack

    def __contains__(self, value): #O(n)
        if self.size == 0:
            return False

        else:
            current = self.head
            while current:
                if current.value == value:
                    return True
                current = current.next
            return False

    def __len__(self): #O(1)
        return self.size
    
    def is_empty(self): #O(1)
        return self.size == 0

    def peek(self): #O(1)
        if self.size == 0:
            raise IndexError("Peek from empty stack")
        return self.head.value

    def push(self, value): #O(1)
        new = StackNode(value)
        new.next = self.head
        self.head = new
        self.size += 1

    def pop(self): #O(1)
        if self.size == 0:
            raise IndexError("Pop from empty stack")
        deleted = self.head
        self.head = self.head.next
        deleted.next = None
        self.size -= 1
        return deleted.value
    
    def clear(self): #O(1)
        self.head = None
        self.size = 0