class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        class Sort:
            def __init__(self, e, p, index):
                self.e = e
                self.p = p
                self.index = index
            def __lt__(self, o):
                return self.e < o.e
            
        
        class Tmp:
            def __init__(self, e, p, index):
                self.e = e
                self.p = p
                self.index = index
            def __lt__(self, o):
                if self.p != o.p:
                    return self.p < o.p
                return self.index < o.index
        
        arr = []
        for i in range(len(tasks)):
            arr.append(Sort(tasks[i][0], tasks[i][1], i))
        arr.sort()
        for i in arr:
            print(i.e, i.p, i.index)

        i = 0
        find = arr[0].e
        pq = []
        res = []
        while i < len(arr):
            print(f"find {find}")
            while i < len(arr) and arr[i].e <= find:
                heapq.heappush(pq, Tmp(arr[i].e, arr[i].p, arr[i].index))
                i += 1
            if not pq and i < len(arr):
                find = arr[i].e
                continue
            ref = heapq.heappop(pq)
            print(f"ref {ref.e} {ref.p} {ref.index}")
            res.append(ref.index)
            find += ref.p
        
        #print(pq)
        while pq:
            res.append(heapq.heappop(pq).index)


        return res
