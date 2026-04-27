class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            #print(i)
            if nums[i] <= 0 or nums[i] > len(nums):
                i += 1
                continue
            if i == nums[i]-1:
                i += 1
                continue
            while True:
                new_pos = nums[i]-1
                if nums[i] <= 0 or nums[i] > len(nums) or nums[new_pos] == nums[i]:
                    break
                tmp = nums[i]
                nums[i] = nums[new_pos]
                nums[new_pos] = tmp
            i += 1
        #print(nums)
        start = 1
        for i in range(len(nums)):
            if nums[i] != start:
                return start
            start += 1
        return start





            