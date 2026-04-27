class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i = 0
        j = 0
        while i < len(nums) and nums[i] < 0:
            i += 1
        while j < len(nums) and nums[j] >= 0:
            j += 1
        
        res = []
        while i < len(nums) and j < len(nums):
            res.append(nums[i])
            i += 1
            while i < len(nums) and nums[i] < 0:
                i += 1
            res.append(nums[j])
            j += 1
            while j < len(nums) and nums[j] >= 0:
                j += 1
        
        return res

        
