class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def f(k):
            left = 0
            d = {}
            res = 0
            for i in range(len(nums)):
                d[nums[i]] = d.get(nums[i], 0)+1
                while len(d) > k:
                    d[nums[left]] -= 1
                    if d[nums[left]] == 0:
                        del d[nums[left]]
                    left += 1
                res += i-left+1
            return res
        return f(k)-f(k-1)
