# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        d = dummy

        c = head
        p = None
        length = 0
        while c:
            length += 1
            c.prev = p
            p = c
            if not c.next:
                break
            c = c.next
        print(length)
        alt = True
        count = 0
        curr = head
        back = c
        while True:
            if alt:
                tmp = curr.next
                d.next = curr
                curr.next = None
                d = d.next
                curr = tmp
                
            else:
                tmp = back.prev
                d.next = back
                back.next = None
                d = d.next
                back = tmp
            count += 1
            alt = not alt
            if count == length:
                break
        head = dummy.next