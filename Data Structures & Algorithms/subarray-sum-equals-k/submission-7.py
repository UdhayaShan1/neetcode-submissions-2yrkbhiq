class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = {0 : 1}
        total = 0
        res = 0
        for i in range(len(nums)):
            #print(pre)
            total += nums[i]
            find = total-k
            #print(total, find)
            res += pre.get(find, 0)
            pre[total] = pre.get(total, 0)+1
        return res

