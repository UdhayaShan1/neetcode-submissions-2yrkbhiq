class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = 1
        e = max(piles)
        res = float('inf')
        while s <= e:
            mid = (s+e)//2
            ref = 0
            for i in piles:
                ref += math.ceil(i/mid)
            if ref > h:
                s = mid+1
            else:
                res = min(res, mid)
                e = mid-1
        return res
