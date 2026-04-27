class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #weights.sort()
        start = max(weights)
        end = sum(weights)
        res = float('inf')
        while start <= end:
            mid = (start+end)//2
            d = 1
            curr = 0
            for i in range(len(weights)):
                curr += weights[i]
                if curr > mid:
                    d += 1
                    curr = weights[i]
            #print(d)
            if d > days:
                start = mid+1
            else:
                res = min(res, mid)
                end = mid-1
        return res
