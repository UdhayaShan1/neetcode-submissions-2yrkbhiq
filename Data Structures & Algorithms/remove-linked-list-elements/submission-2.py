# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        d = ListNode()
        d1 = d

        curr = head
        while curr:
            if curr.val == val:
                curr = curr.next
            else:
                d.next = curr
                tmp = curr.next
                curr.next = None
                curr = tmp
                d = d.next
        return d1.next