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
        
        chk = 0
        chk2 = 0
        for i in nums:
            if i == cand1:
                chk += 1
            elif i == cand2:
                chk2 += 1
        res = []
        #print(cand1, chk, cand2, chk2)
        for i in [(cand1, chk), (cand2, chk2)]:
            if i[1] > len(nums)//3:
                res.append(i[0])
        return res