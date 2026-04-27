class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        res = 0
        while start <= end:
            mid = (start+end)//2
            if mid*mid <= x:
                res = max(res, mid)
                start = mid+1
            else:
                end = mid-1
        return res


