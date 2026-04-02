class Tmp:
    def __init__(self, v):
        self.v = v
    def __lt__(self, o):
        return self.v < o.v

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = []
        for i in range(len(nums)):
            if len(self.pq) < k:
                heapq.heappush(self.pq, Tmp(nums[i]))
            else:
                if nums[i] >= self.pq[0].v:
                    heapq.heappop(self.pq)
                    heapq.heappush(self.pq, Tmp(nums[i]))

        

    def add(self, val: int) -> int:
        if len(self.pq) < self.k:
            heapq.heappush(self.pq, Tmp(val))
        else:
            if val >= self.pq[0].v:
                heapq.heappop(self.pq)
                heapq.heappush(self.pq, Tmp(val))
        return self.pq[0].v
        
