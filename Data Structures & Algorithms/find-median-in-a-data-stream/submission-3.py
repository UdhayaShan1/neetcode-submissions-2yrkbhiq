class Min:
    def __init__(self, v):
        self.v = v
    def __lt__(self, o):
        return self.v < o.v
class Max:
    def __init__(self, v):
        self.v = v
    def __lt__(self, o):
        return self.v > o.v 


class MedianFinder:

    def __init__(self):
        self.pq1 = []
        self.pq2 = []
    
    def balance(self):
        while abs(len(self.pq1)-len(self.pq2)) > 1:
            if len(self.pq1) > len(self.pq2):
                heapq.heappush(self.pq2, Min(heapq.heappop(self.pq1).v))
            else:
                heapq.heappush(self.pq1, Max(heapq.heappop(self.pq2).v))


    def addNum(self, num: int) -> None:
        if not self.pq1 and not self.pq2:
            heapq.heappush(self.pq1, Max(num))
            return
        if self.pq1 and num <= self.pq1[0].v:
            heapq.heappush(self.pq1, Max(num))
        else:
            heapq.heappush(self.pq2, Min(num))
        self.balance()

        

    def findMedian(self) -> float:
        # print(len(self.pq1), len(self.pq2))
        # if self.pq1:
        #     print('@', self.pq1[0].v)
        # if self.pq2:
        #     print('%', self.pq2[0].v)

        total = len(self.pq1) + len(self.pq2)
        if total % 2 == 0:
            return (self.pq1[0].v+self.pq2[0].v)/2
        if len(self.pq1) > len(self.pq2):
            return self.pq1[0].v
        return self.pq2[0].v

        
        