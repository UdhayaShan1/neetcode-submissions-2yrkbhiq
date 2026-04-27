class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = {}
        chk = {}
        for i in range(len(nums)):
            chk[nums[i]] = i
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                find = 0-(nums[i]+nums[j])
                if find in chk and chk[find] > j:
                    ref = [nums[i], nums[j], find]
                    ref.sort()
                    res[tuple(ref)] = 1
        
        final = [list(i) for i in res]
        return final

        