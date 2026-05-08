class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        p = {0:1}
        curr = 0 
        res = 0
        for i in range(len(nums)):
            curr += nums[i]
            find = curr-goal
            res += p.get(find, 0)
            p[curr] = p.get(curr, 0)+1
        return res
