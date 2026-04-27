class Solution:
    def arrangeCoins(self, n: int) -> int:
        start = 1
        end = n
        res = 0
        while start <= end:
            mid = (start+end)//2
            ref = mid*(mid+1)//2
            if ref <= n:
                res = max(res, mid)
                start = mid+1
            else:
                end = mid-1
        return res
