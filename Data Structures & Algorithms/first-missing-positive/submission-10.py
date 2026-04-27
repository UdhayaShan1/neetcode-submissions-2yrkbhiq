class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #r = [1, len(nums)]
        for i in range(len(nums)):
            if nums[i] == i+1:
                continue
            #swap
            while nums[i] >= 1 and nums[i] <= len(nums) and nums[i] != i-1:
                print(nums)
                og = nums[i]
                og_pos = og-1
                if nums[i] == nums[og_pos]:
                    break
                nums[i], nums[og_pos] = nums[og_pos], nums[i]
        print(nums)
        ref = 1
        for i in range(len(nums)):
            if nums[i] < 1 or nums[i] > len(nums):
                continue
            if nums[i] != ref:
                return ref
            ref += 1
        return ref


