class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        thres = len(nums)//3
        nums.sort()
        i = 0
        while i < len(nums):
            count = 0
            ref = nums[i]
            j = i
            while j < len(nums) and nums[j] == ref:
                count += 1
                j += 1
            if count > thres:
                res.append(ref)
            if j > i:
                i = j
            else:
                i += 1
        return res   