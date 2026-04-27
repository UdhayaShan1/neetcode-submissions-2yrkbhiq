class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        chk = {}
        for i in range(len(nums)):
            chk[nums[i]] = i
        for i in range(len(nums)):
            find = target-nums[i]
            if find not in chk or chk[find] == i:
                continue
            return [i, chk[find]]
            