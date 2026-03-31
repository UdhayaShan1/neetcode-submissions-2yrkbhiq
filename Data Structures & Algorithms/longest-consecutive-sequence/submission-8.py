class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for i in nums:
            if i-1 in s:
                continue
            chk = 0
            ref = i
            while ref in s:
                ref += 1
                chk += 1
            res = max(res, chk)
        return res
            
                