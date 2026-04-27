# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        pos = length - n - 1
        curr = head
        index = 0
        if pos == -1:
            return head.next
        print(pos)
        while curr:
            if index == pos:
                curr.next = curr.next.next
            curr = curr.next
            index += 1
        return head
