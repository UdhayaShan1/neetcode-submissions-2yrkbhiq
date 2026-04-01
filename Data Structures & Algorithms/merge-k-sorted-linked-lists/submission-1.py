# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        class Tmp:
            def __init__(self, node):
                self.n = node
            def __lt__(self, o):
                return self.n.val < o.n.val
        
        pq = []
        for i in lists:
            heapq.heappush(pq, Tmp(i))

        d = ListNode()
        res = d
        while pq:
            x = heapq.heappop(pq)
            d.next = x.n
            d = d.next
            tmp = x.n.next
            x.n.next = None
            if tmp:
                heapq.heappush(pq, Tmp(tmp))
        #print(res[0])
        return res.next
