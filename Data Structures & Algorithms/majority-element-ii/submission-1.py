class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = 0
        cand2 = 0
        count1 = 0
        count2 = 0
        for i in nums:
            if i == cand1:
                count1 += 1
            elif i == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = i
                count1 = 1
            elif count2 == 0:
                cand2 = i
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        #print(cand1, cand2, count1, count2)

        res = []
        c1 = nums.count(cand1)
        c2 = nums.count(cand2)
        if c1 > len(nums)//3:
            res.append(cand1)
        if c2 > len(nums)//3:
            res.append(cand2)
        return res
