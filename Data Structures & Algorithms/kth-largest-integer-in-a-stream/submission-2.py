class Tmp:
    def __init__(self, val):
        self.val = val
    def __lt__(self, o):
        return self.val < o.val

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = []
        for i in nums:
            if len(self.pq) < self.k:
                heapq.heappush(self.pq, Tmp(i))
            else:
                if i > self.pq[0].val:
                    heapq.heappop(self.pq)
                    heapq.heappush(self.pq, Tmp(i))

        

    def add(self, val: int) -> int:
        if len(self.pq) < self.k:
            heapq.heappush(self.pq, Tmp(val))
        else:
            if val > self.pq[0].val:
                heapq.heappop(self.pq)
                heapq.heappush(self.pq, Tmp(val))
        return self.pq[0].val
        
