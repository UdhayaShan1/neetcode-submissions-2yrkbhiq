class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1]+nums[i])
        #print(prefix)
        chk = {}
        chk[0] = 1
        res = 0
        for i in prefix:
            find = i-goal
            res += chk.get(find, 0)

            chk[i] = chk.get(i, 0)+1
        return res
