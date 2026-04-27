# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()

        dummy = d
        d1 = list1
        d2 = list2
        while d1 and d2:
            if d1.val < d2.val:
                d.next = d1
                d1 = d1.next
            else:
                d.next = d2
                d2 = d2.next
            d = d.next
        #print(d1.val, d2)
        if d1:
            d.next = d1
        if d2:
            d.next = d2
        return dummy.next
            
