from typing import Optional

from data_structures.Linked_Lists.linked_list import ListNode

class Solution:
    def __init__(self):
        self.head = None

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        
        new_node = ListNode(x + y)
        
        carry = 0

        if new_node.val > 9:
            carry = new_node.val//10
            new_node.val -= carry*10
        
        self.head = new_node

        previous_node = new_node

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

        if l1 is None and l2 is None:
            if carry != 0:
                carry_node = ListNode(carry)
                previous_node.next = carry_node
            return self.head

        while True:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            new_node = ListNode(x + y + carry)

            carry = 0

            if new_node.val > 9:
                carry = new_node.val//10
                new_node.val -= carry*10
            previous_node.next = new_node
            previous_node = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if l1 is None and l2 is None:
                if carry != 0:
                    carry_node = ListNode(carry)
                    previous_node.next = carry_node
                return self.head