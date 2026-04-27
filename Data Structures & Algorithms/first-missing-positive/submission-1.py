class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            #print(nums, i)
            start = i
            while nums[start] >= 1 and nums[start] <= len(nums):
                #print(i, nums)
                ind = nums[start]-1
                if start == ind or nums[start] == nums[ind]:
                    break
                tmp = nums[ind]
                nums[ind] = nums[start]
                nums[start] = tmp
                #start = ind
        # if nums[0] != 1:
        #     return 1
        chk = 1
        for i in range(len(nums)):
            if nums[i] != chk:
                return chk
            chk += 1
        return chk



