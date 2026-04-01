# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        c = head
        while c:
            l += 1
            c = c.next
        find = l-n
        print(find)

        if find == 0:
            return head.next

        l = 0
        c = head
        while c:
            if l+1 == find:
                c.next = c.next.next
            l += 1
            c = c.next
        return head
