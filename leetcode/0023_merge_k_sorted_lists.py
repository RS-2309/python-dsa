from data_structures.Linked_Lists.linked_list import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None

        values = []

        for node in lists:
            while node:
                values.append(node.val)
                node = node.next

        values.sort()

        dummy = ListNode(0)
        current = dummy

        for item in values:
            current.next = ListNode(item)
            current = current.next

        return dummy.next

##########################
#OR
##########################

class Solution:

    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None

        interval = 1

        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self.mergeTwoLists(
                    lists[i],
                    lists[i + interval]
                )

            interval *= 2

        return lists[0]

    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        current.next = list1 if list1 else list2

        return dummy.next