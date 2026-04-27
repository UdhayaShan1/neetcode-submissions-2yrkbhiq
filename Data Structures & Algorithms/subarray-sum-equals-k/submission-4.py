class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i]+prefix[-1])
        chk = {}
        chk[0] = 1
        res = 0
        for i in prefix:
            find = i-k
            res += chk.get(find, 0)
            chk[i] = chk.get(i, 0)+1
        return res
