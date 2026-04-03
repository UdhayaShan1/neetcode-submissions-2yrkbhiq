class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def f(k):
            chk = {}
            left = 0
            res = 0
            for i in range(len(nums)):
                chk[nums[i]] = chk.get(nums[i], 0)+1
                while len(chk) > k:
                    chk[nums[left]] -= 1
                    if chk[nums[left]] == 0:
                        del chk[nums[left]]
                    left += 1
                res += i-left+1
            return res
        return f(k)-f(k-1)
