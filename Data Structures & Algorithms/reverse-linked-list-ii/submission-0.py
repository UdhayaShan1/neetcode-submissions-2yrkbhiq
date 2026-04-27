# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        prev = None
        after = None
        start = None
        end = None
        c = 1
        if left == 1:
            prev = None
        curr = head
        while curr:
            if c == left-1:
                prev = curr
            if c == right:
                after = curr.next
            if c == left:
                start = curr
            if c == right:
                end = curr
            curr = curr.next
            c += 1
        if prev:
            print(prev.val)
        if after:
            print(after.val)
        
        if prev:
            prev.next = end
        t = start.next # 2
        start.next = after # 1->4
        p = start
        while True:
            tmp = t.next
            t.next = p
            if t == end:
                break
            p = t
            t = tmp
        if prev is None:
            head = end
        return head






