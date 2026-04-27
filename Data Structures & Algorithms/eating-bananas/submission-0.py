class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        res = end
        while start <= end:
            mid = (start+end)//2
            count = 0
            for i in piles:
                if i % mid == 0:
                    count += i//mid
                else:
                    count += i//mid + 1
            if count <= h:
                res = min(res, mid)
                end = mid-1
            else:
                start = mid+1
        return res
