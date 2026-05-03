class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for i in nums:
            if i-1 in s:
                continue
            curr = 0
            ref = i
            while ref in s:
                curr += 1
                ref += 1
            res = max(res, curr)
        return res

