class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i in range(len(nums)):
            find = target-nums[i]
            if find in index:
                return [index[find], i]
            index[nums[i]] = i
