# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        c = head
        d1 = ListNode()
        d = d1
        while c:
            while c and c.val == val:
                c = c.next
            d.next = c
            d = d.next
            if c:
                c = c.next
        return d1.next
