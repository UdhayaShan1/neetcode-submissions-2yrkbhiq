class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def f(k):
            if k < 0:
                return 0
            curr = 0
            left = 0
            res = 0
            for i in range(len(nums)):
                curr += nums[i]
                while curr > k:
                    curr -= nums[left]
                    left += 1
                res += i-left+1
            return res
        #print(f(goal), f(goal-1))
        return f(goal)-f(goal-1)
                