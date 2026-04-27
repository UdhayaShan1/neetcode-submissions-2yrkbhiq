class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        chk = {}
        nums.sort()
        for i in range(len(nums)):
            chk[nums[i]] = i
        
        res = []
        #print(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    curr = nums[i]+nums[j]+nums[k]
                    #print(curr, i, j, k)
                    find = target-curr
                    if find in chk and chk[find] > k:
                        #print("@", find,i ,j ,k)
                        r = [nums[i], nums[j], nums[k], find]
                        r.sort()
                        ref = tuple(r)
                        if ref not in chk:
                            res.append(r)
                        chk[ref] = 1
                        #res.append(r)
        return res
