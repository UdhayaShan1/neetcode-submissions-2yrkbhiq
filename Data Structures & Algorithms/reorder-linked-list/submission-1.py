# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        start = head
        end = head
        tmp = None
        length = 0
        while True:
            end.prev = tmp
            length += 1
            if end.next == None:
                break
            tmp = end
            end = end.next
        #print(start.val, end.val, prev[end].val, length)
        new = ListNode()
        c = new
        #print(c.val)
        turns = True
        l = 0
        while l < length:
            #print(new.val, start.val, end.val, l, length, "#")
            if turns:
                new.next = start
                start = start.next
            else:
                new.next = end
                end = end.prev
            new = new.next
            l += 1
            turns = not turns
        new.next = None
        #print(c.val, c.next.val, c.next.next.val, c.next.next.next.val, c.next.next.next.next.val)
        head = c.next


        

