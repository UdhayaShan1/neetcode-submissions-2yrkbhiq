class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        curr = 0
        res = 0
        for i in range(len(nums)):
            curr += 1-nums[i]

            while curr > k:
                curr -= (1-nums[left])
                left += 1
            res = max(res, i-left+1)
        return res
