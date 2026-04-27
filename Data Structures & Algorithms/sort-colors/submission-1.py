class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        j = 0
        k = len(nums)-1
        while j <= k:
            if nums[j] == 0:
                nums[j] = nums[i]
                nums[i] = 0
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[j] = nums[k]
                nums[k] = 2
                k -= 1
        
        