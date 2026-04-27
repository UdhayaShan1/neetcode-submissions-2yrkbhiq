# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        back = head
        prev = None
        while True:
            if back.next is None:
                back.prev = prev
                break
            back.prev = prev
            prev = back
            back = back.next
        #print(head.val, back.val, back.prev.val)

        d = head
        while d and back:
            if d.val != back.val:
                return False
            d = d.next
            back = back.prev
        return True