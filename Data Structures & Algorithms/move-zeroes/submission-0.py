class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] != 0:
                i += 1
                j = max(i, j)
                continue
            while j < len(nums) and nums[j] == 0:
                j += 1

            if j < len(nums):
                nums[i] = nums[j]
                nums[j] = 0
            i += 1
        print(nums)

            
        