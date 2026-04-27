# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None
        while True:
            curr.prev = prev
            if curr.next == None:
                break
            prev = curr
            curr = curr.next
        for i in range(n-1):
            curr = curr.prev
        
        #print(curr.val)
        if curr == head:
            return curr.next
        before = curr.prev
        before.next = curr.next
        return head

