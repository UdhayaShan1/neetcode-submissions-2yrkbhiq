class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = None
        c2 = None
        count1 = 0
        count2 = 0
        for i in range(len(nums)):
            if nums[i] == c1:
                count1 += 1
            elif nums[i] == c2:
                count2 += 1
            elif count1 == 0:
                c1 = nums[i]
                count1 = 1
            elif count2 == 0:
                c2 = nums[i]
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        #print(c1, c2)
        cands = [c1, c2]
        threshold = len(nums)//3
        res = []
        for i in cands:
            c = 0
            for j in nums:
                if j == i:
                    c += 1
            if c > threshold:
                res.append(i)
        return res

