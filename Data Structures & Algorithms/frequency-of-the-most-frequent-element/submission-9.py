class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        curr = 0
        res = 0
        for i in range(len(nums)):
            curr += nums[i]
            ref = nums[i]*(i-left+1)-curr
            while True:
                ref = nums[i]*(i-left+1)-curr
                if ref <= k:
                    break
                curr -= nums[left]
                left += 1
            if ref <= k:
                res = max(res, i-left+1)
        return res
