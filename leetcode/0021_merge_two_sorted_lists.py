from data_structures.Linked_Lists.linked_list import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        current_1 = list1
        current_2 = list2

        if current_1 is None:
            return current_2

        if current_2 is None:
            return current_1

        head = current_1 if min(current_1.val, current_2.val) == current_1.val else current_2

        old = 0

        while True:
            less = current_1 if min(current_1.val, current_2.val) == current_1.val else current_2
            more = current_2 if max(current_1.val, current_2.val) == current_2.val else current_1

            if old and (less == current_1):
                old.next = less

                less_next = less.next
                less.next = more

                current_1 = less_next
                current_2 = more

                old = less

                if current_1 is None:
                    break

            else:
                old = less

                less_next = less.next
                less.next = more

                current_1 = less_next
                current_2 = more
    
                if current_1 is None:
                    break

        return head