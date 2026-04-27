# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        prev = None
        c = head
        length = 0
        while True:
            length += 1
            tmp = c.next
            c.prev = prev
            prev = c
            if tmp:
                c = tmp
            else:
                break
        print(length, c.val)

        dummy = ListNode()
        d = dummy

        hmm = True
        chk = 0
        c1 = head
        while True:
            chk += 1
            if chk == length+1:
                break
            #print(c.val, )
            if hmm:
                tmp = c1.next
                c1.next = None
                d.next = c1
                c1 = tmp
            else:
                tmp = c.prev
                c.next = None
                d.next = c
                c = tmp
            d = d.next
            hmm = not hmm
        head = dummy.next
            
        
