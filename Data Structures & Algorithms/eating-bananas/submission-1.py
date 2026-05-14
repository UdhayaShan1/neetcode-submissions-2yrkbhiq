class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = 1
        e = max(piles)
        res = float('inf')
        while s <= e:
            mid = (s+e)//2
            c = 0
            for i in piles:
                c += math.ceil(i/mid)
            if c <= h:
                res = mid
                e = mid-1
            else:
                s = mid+1
        return res
                