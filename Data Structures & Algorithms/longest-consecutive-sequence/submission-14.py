class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set(nums)
        for i in nums:
            if i-1 in s:
                continue
            r = 0
            ref = i
            while ref in s:
                r += 1
                ref += 1
            res = max(r, res)
        return res
            