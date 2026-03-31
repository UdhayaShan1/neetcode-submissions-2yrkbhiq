class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        pos = {}
        for i in range(len(nums)):
            pos[nums[i]] = i
        res = []
        ref = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                s = nums[i]+nums[j]
                find = -s
                if find in pos and pos[find] != i and pos[find] != j:
                    r = [nums[i], nums[j], find]
                    r.sort()
                    r = tuple(r)
                    if r in ref:
                        continue
                    ref[r] = True
                    res.append(list(r))
        return res

