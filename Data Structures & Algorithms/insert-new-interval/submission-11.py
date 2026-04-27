class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = 0
        end = len(intervals)-1
        res = -1
        while start <= end:
            mid = (start+end)//2
            ref = intervals[mid]
            if ref[0] <= newInterval[0]:
                res = max(res, mid)
                start = mid+1
            else:
                end = mid-1
        print(res)

        new = []
        if res == -1:
            new = [newInterval]+intervals
        else:
            for i in range(len(intervals)):
                new.append(intervals[i])
                if i == res:
                    new.append(newInterval)
            print(new)
        
        new2 = []
        for i in new:
            new2.append(i)
            while len(new2) > 1 and new2[-1][0] <= new2[-2][1]:
                ref = [min(new2[-1][0], new2[-2][0]), max(new2[-1][1], new2[-2][1])]
                new2.pop()
                new2.pop()
                new2.append(ref)
        return new2
            
                