class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] % 2 == 0:
                i += 1
                j = max(i, j)
                continue
            
            while j < len(nums) and nums[j] % 2 != 0:
                j += 1
            
            if j < len(nums):
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
            i += 1
        return nums
            