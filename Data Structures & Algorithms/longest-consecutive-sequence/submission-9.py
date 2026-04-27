class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        d = set(nums)
        r = 0
        for i in nums:
            if i in s:
                continue
            res = 0
            ref = i
            while ref in d:
                res += 1
                ref += 1
                s.add(ref)
            r = max(r, res)
        return r
            
