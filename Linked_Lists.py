class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None #The starting point of the LinkedList
    
    def __repr__(self):
        if self.head is None:
            return "[]"
        else:
            node = self.head
            
            return_string = f"[{node.value}"

            while node.next is not None:
                node = node.next
                return_string += f", {node.value}"
            return_string += f"]"
            
            return return_string

    def __contains__(self, value):
        node = self.head

        while node is not None:
            if node.value == value:
                return True
            node = node.next
        return False

    def __len__(self):
        if self.head is None:
            return 0
        else:
            count = 0
            node = self.head
            while node is not None:
                count += 1
                node = node.next
            return count

    def append(self, value):
        if self.head == None:
            self.head = ListNode(value)
        else:
            last = self.head
            while last.next is not None:
                last = last.next
            last.next = ListNode(value)

    def prepend(self, value):
        if self.head == None:
            self.head = ListNode(value)
        else:
            node = ListNode(value)
            node.next = self.head
            self.head = node

    def insert(self, value, index):
        if index > len(self):
            raise ValueError("Index out of Bounds.")
        elif index == 0:
            self.prepend(value)
        elif index == len(self):
            self.append(value)
        else:
            initial_index = 1
            node = self.head
            new_node = ListNode(value)
            while node is not None:
                if initial_index == index:
                    new_node.next = node.next
                    node.next = new_node
                    break
                initial_index += 1
                node = node.next

    def delete(self, value):
        node = self.head
        index = 0
        if node is None:
            raise ValueError("Cannot delete from an empty list.")
        if node.value == value:
            deleted_node = node
            self.head = node.next
            deleted_node.next = None
        if node.value != value:
            while index != (len(self)-1):
                index += 1
                if node.next.value == value:
                    deleted_node = node.next
                    node.next = node.next.next
                    deleted_node.next = None
                    break
                node = node.next
        if index == (len(self)-1):
            raise ValueError("The value doesn't exist.")
    
    def pop(self, index=-1):
        if self.head is None:
            raise ValueError("Cannot pop from empty list.")
        if index == -1:
            index = len(self) - 1
        if index >= len(self):
            raise ValueError("Index out of Bounds.")
        elif index == 0:
            deleted_node = self.head
            self.head = self.head.next
            deleted_node.next = None
            return deleted_node.value
        else:
            node = self.head
            initial_index = 1
            while True:
                if initial_index == index:
                    deleted_node = node.next
                    node.next = node.next.next
                    deleted_node.next = None
                    return deleted_node.value
                else:
                    initial_index += 1
                    node = node.next
    
    def reverse(self):
        if self.head is None or self.head.next is None:
            pass
        else:
            previous_node = self.head
            node = self.head.next
            next_node = self.head.next.next
            self.head.next = None
            while node:
                node.next = previous_node
                previous_node = node
                node = next_node
                if node is not None:
                    next_node = node.next
            self.head = previous_node
            
    def get(self, index):
        if index >= len(self):
            raise ValueError("Index out of Bounds.")
        else:
            node = self.head
            initial_index = 0
            while True:
                if initial_index == index:
                    return node.value
                node = node.next
                initial_index += 1
                    

if __name__ == "__main__":
    l = LinkedList()

    l.append(10)
    l.append(20)
    l.append(30)
    l.prepend(5)

    l.insert(40, 2)

    l.delete(5)

    l.reverse()

    print(l)