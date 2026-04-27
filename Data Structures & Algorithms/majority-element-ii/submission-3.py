class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = None
        cand2 = None
        count1 = 0
        count2 = 0
        for i in range(len(nums)):
            if nums[i] == cand1:
                count1 += 1
            elif nums[i] == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = nums[i]
                count1 = 1
            elif count2 == 0:
                cand2 = nums[i]
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        res = []
        c1 = 0
        c2 = 0
        for i in nums:
            if i == cand1:
                c1 += 1
            if i == cand2:
                c2 += 1
        res = []
        if c1 > len(nums)//3:
            res.append(cand1)
        if c2 > len(nums)//3:
            res.append(cand2)
        #print(cand1,cand2,count1, count2)
        return res
