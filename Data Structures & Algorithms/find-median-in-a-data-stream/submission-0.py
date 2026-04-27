import heapq

class Tmp1:
    def __init__(self, v):
        self.v = v
    def __lt__(self, o):
        return self.v > o.v

class Tmp2:
    def __init__(self, v):
        self.v = v
    def __lt__(self, o):
        return self.v < o.v 


class MedianFinder:

    def __init__(self):
        self.pq1 = []
        self.pq2 = []
        

    def addNum(self, num: int) -> None:
        if len(self.pq1) == 0:
            heapq.heappush(self.pq1, Tmp1(num))
        else:
            max1 = self.pq1[0].v
            if num > max1:
                heapq.heappush(self.pq2, Tmp2(num))
            else:
                heapq.heappush(self.pq1, Tmp1(num))
        
        if len(self.pq1) - 1 > len(self.pq2):
            max1 = heapq.heappop(self.pq1).v
            heapq.heappush(self.pq2, Tmp2(max1))
        elif len(self.pq2) - 1 > len(self.pq1):
            min1 = heapq.heappop(self.pq2).v
            heapq.heappush(self.pq1, Tmp1(min1))



        

    def findMedian(self) -> float:
        if len(self.pq1) == len(self.pq2):
            return (self.pq1[0].v+self.pq2[0].v)/2
        if len(self.pq1) > len(self.pq2):
            return self.pq1[0].v
        return self.pq2[0].v

        
        