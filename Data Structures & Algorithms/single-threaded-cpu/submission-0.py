class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        class Tmp:
            def __init__(self, e, p, i):
                self.e = e
                self.p = p
                self.i = i
            def __lt__(self, o):
                return self.e < o.e
        class Tmp2:
            def __init__(self, e, p, i):
                self.e = e
                self.p = p
                self.i = i
            def __lt__(self, o):
                if self.p != o.p:
                    return self.p < o.p
                return self.i < o.i
        arr = []
        pq = []
        time = 0
        import heapq
        for i in range(len(tasks)):
            arr.append(Tmp(tasks[i][0], tasks[i][1], i))
        arr.sort()

        i = 0
        res = []
        while True:
            if i >= len(arr) and not pq:
                break
            if i < len(arr) and time < arr[i].e:
                time = arr[i].e
                continue
            
            while i < len(arr) and time >= arr[i].e:
                heapq.heappush(pq, Tmp2(arr[i].e, arr[i].p, arr[i].i))
                i += 1
            if pq:
                best = heapq.heappop(pq)
                time += best.p
                res.append(best.i)

        #print(len(pq), pq[0].i)

        return res
                

