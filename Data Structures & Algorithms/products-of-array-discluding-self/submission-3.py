class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1]
        for i in range(1, len(nums)):
            p.append(p[-1]*nums[i-1])
        s = [1]
        for i in range(len(nums)-2, -1, -1):
            s.append(nums[i+1]*s[-1])
        s = s[::-1]
        #print(p, s)
        res = []
        for i in range(len(nums)):
            res.append(p[i]*s[i])
        return res
