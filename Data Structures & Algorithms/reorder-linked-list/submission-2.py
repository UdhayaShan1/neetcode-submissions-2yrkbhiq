# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        c = head
        end = head
        prev = None
        length = 0
        while True:
            end.prev = prev
            if end.next == None:
                break
            prev = end
            end = end.next
            length += 1
        
        length += 1
        #print(length)

        d = ListNode()
        tmp = d
        l = 0
        while l < length:
            if l % 2 == 0:
                d.next = c
                c = c.next
                d = d.next
            else:
                d.next = end
                end = end.prev
                d = d.next
            l += 1
        d.next = None
        head = tmp.next
        
        