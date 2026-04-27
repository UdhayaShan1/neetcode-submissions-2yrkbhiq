class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        chk = {}
        for i in range(len(nums)):
            find = target-nums[i]
            if find not in chk:
                chk[nums[i]] = i
            else:
                return [chk[find], i]
