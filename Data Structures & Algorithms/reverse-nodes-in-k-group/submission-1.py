# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        curr = head
        
        prev = None
        while curr:
            start = curr
            count = 0
            while curr and count < k-1:
                curr = curr.next
                count += 1
            #print(curr.val, count)
            if count < k-1 or not curr:
                break 
            
            last_remember = curr
            tmp_next = curr.next

            
            curr = start.next #2
            start.next = tmp_next # 1 -> 4
            if prev:
                prev.next = last_remember # prev -> 3
            else:
                head = last_remember
            prev = start # prev = 1
            p = start
            while curr:
                tmp = curr.next
                curr.next = p
                if curr == last_remember:
                    break
                p = curr
                curr = tmp
            
            curr = tmp_next
                



        return head

