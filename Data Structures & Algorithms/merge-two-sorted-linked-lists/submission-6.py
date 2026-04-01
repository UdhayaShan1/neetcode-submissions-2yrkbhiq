# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = ListNode()
        d = l
        while list1 and list2:
            if list1.val < list2.val:
                l.next = list1
                tmp = list1.next
                list1.next = None
                list1 = tmp
            else:
                l.next = list2
                tmp = list2.next
                list2.next = None
                list2 = tmp
            l = l.next
        if list1:
            l.next = list1
        if list2:
            l.next = list2
        return d.next