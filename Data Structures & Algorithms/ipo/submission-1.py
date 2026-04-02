class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        class Tmp:
            def __init__(self, p, c):
                self.p = p
                self.c = c
            def __lt__(self, o):
                return self.p > o.p
        pq = []

        class Node:
            def __init__(self, p, c):
                self.p = p
                self.c = c
            def __lt__(self, o):
                return self.c < o.c
        
        arr = []
        for i in range(len(profits)):
            arr.append(Node(profits[i], capital[i]))
        arr.sort()
        for i in arr:
            print('##', i.p, i.c)

        i = 0
        res = w
        while True:
            while i < len(arr) and w >= arr[i].c:
                heapq.heappush(pq, Tmp(arr[i].p, arr[i].c))
                i += 1
            print(i, w, len(pq))
            if not pq or k == 0:
                return res
            
            r = heapq.heappop(pq).p
            res += r
            w += r
            k -= 1
            print('after', i, w, len(pq))
        
            
