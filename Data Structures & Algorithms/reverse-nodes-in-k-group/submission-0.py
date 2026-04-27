# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        


        d = ListNode(next=head)

        curr = d.next
        #print(curr.val)
        prev = d
        l = 0
        print(length)
        while curr:
            #l += 1
            # print(l, curr.val)
            # if length-l < k-1:
            #     break
            p = prev
            first = curr
            #print(first.val, p.val)
            c = curr
            bad = False
            for i in range(k):
                if c is None:
                    bad = True
                    break
                c = c.next
            if bad:
                break



            for i in range(k):
                l += 1
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            #print(prev.val, prev.next.val, prev.next.next.val, p.val, curr.val)
            #print(curr.val, first.val)
            first.next = curr
            p.next = prev
            prev = first
        return d.next

