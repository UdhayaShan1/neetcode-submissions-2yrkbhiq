class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        pos = {}
        for i in range(len(nums)):
            pos[nums[i]] = i
        res = []
        s = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                find = 0-(nums[i]+nums[j])
                if pos.get(find, -1) > j:
                    ans = (nums[i], nums[j], find)
                    if ans in s:
                        continue
                    s.add(ans)
                    res.append(ans)
        return res
