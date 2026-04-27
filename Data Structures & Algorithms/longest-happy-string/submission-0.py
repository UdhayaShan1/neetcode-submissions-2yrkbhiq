class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        chk = []
        class Tmp:
            def __init__(self, c, v):
                self.c = c
                self.v = v
            def __lt__(self, o):
                return self.v > o.v
        
        count = {"a" : a, "b" : b, "c" : c}
        for i in count:
            if count[i] > 0:
                heapq.heappush(chk, Tmp(i, count[i]))
        
        res = ""
        while chk:
            #print(res, chk[0].c)
            tmp = heapq.heappop(chk)
            if len(res) < 2:
                res += tmp.c
                if tmp.v-1 > 0:
                    heapq.heappush(chk, Tmp(tmp.c, tmp.v-1))
            else:
                if res[-1] == tmp.c and res[-2] == tmp.c:
                    if not chk:
                        break
                    tmp1 = heapq.heappop(chk)
                    res += tmp1.c
                    if tmp1.v-1 > 0:
                        heapq.heappush(chk, Tmp(tmp1.c, tmp1.v-1))
                    heapq.heappush(chk, tmp)
                else:
                    res += tmp.c
                    if tmp.v-1 > 0:
                        heapq.heappush(chk, Tmp(tmp.c, tmp.v-1))
        return res
                    
                    
