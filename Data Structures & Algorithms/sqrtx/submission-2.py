class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        s = 1
        e = x
        while s <= e:
            mid = (s+e)//2
            if mid**2 <= x:
                res = mid
                s = mid+1
            else:
                e = mid-1
        return res