class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for i in range(1, len(nums)):
            pre.append(nums[i-1]*pre[-1])
        suff = [1]
        for i in range(len(nums)-2, -1, -1):
            suff.append(nums[i+1]*suff[-1])
        suff = suff[::-1]

        #print(pre, suff)

        res = []
        for i in range(len(nums)):
            res.append(pre[i]*suff[i])
        return res