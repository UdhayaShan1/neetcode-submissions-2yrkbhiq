class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = None
        cand2 = None
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
        pos = [0, 0]
        for i in nums:
            if i == cand1:
                pos[0] += 1
            elif i == cand2:
                pos[1] += 1
        print(cand1, cand2)
        res = []
        if pos[0] > len(nums)//3:
            res.append(cand1)
        if pos[1] > len(nums)//3:
            res.append(cand2)
        return res
