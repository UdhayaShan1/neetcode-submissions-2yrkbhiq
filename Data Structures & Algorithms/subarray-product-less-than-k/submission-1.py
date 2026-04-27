class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        product = 1
        res = 0
        for i in range(len(nums)):
            product *= nums[i]
            
            while left < len(nums) and product >= k:
                product //= nums[left]
                left += 1
            #print(left, i, product)
            if product > 0:
                res += max(0, i-left+1)
        return res
            
