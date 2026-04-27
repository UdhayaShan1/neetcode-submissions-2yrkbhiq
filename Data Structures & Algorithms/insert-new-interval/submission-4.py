class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        pos = -1
        for i in range(len(intervals)):
            ref = intervals[i]
            if ref[0] <= newInterval[0]:
                pos = i
        res = []
        #print(pos)
        if pos == -1:
            res = [newInterval]
        for i in range(len(intervals)):
            res.append(intervals[i])
            if i == pos:
                res.append(newInterval)
        #print(res)

        ref = res[0]
        new = [ref]
        for i in range(1, len(res)):
            chk = res[i]
            if ref[1] >= chk[0]:
                ref[0] = min(ref[0], chk[0])
                ref[1] = max(ref[1], chk[1])
            else:
                new.append(chk)
                ref = new[-1]
        return new
                
        
