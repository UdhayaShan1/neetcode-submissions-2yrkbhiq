class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] <= 0 or nums[i] > len(nums):
                i += 1
                continue
            while True:
                #print(i, nums)
                if nums[i]-1 == i or nums[i] <= 0 or nums[i] > len(nums):
                    break
                ref = nums[nums[i]-1]
                tmp = nums[i]
                if ref == tmp:
                    break
                nums[i] = ref
                nums[tmp-1] = tmp
            i += 1
        
        l = 1
        for i in nums:
            if i == l:
                l += 1
            else:
                return l
        return l

            

