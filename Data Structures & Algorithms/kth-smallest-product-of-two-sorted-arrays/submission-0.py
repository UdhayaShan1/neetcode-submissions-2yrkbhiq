from bisect import bisect_left, bisect_right
from typing import List

def ceil_div(a: int, b: int) -> int:
    # works for any signs
    return -((-a) // b)

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        A, B = nums1, nums2

        def count_leq(x: int) -> int:
            cnt = 0
            for a in A:
                if a > 0:
                    cnt += bisect_right(B, x // a)
                elif a < 0:
                    cnt += len(B) - bisect_left(B, ceil_div(x, a))
                else:  # a == 0
                    if x >= 0:
                        cnt += len(B)
            return cnt

        lo = min(A[0]*B[0], A[0]*B[-1], A[-1]*B[0], A[-1]*B[-1])
        hi = max(A[0]*B[0], A[0]*B[-1], A[-1]*B[0], A[-1]*B[-1])

        res = float('inf')
        while lo <= hi:
            mid = (lo + hi) // 2
            if count_leq(mid) >= k:
                res = min(res, mid)
                hi = mid-1
            else:
                lo = mid + 1
        return res
