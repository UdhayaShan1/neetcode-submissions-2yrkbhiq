class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        chk = {}
        def dfs(k1, arr):
            if k1 >= len(nums):
                arr2 = arr[:]
                arr2.sort()
                if tuple(arr2) in chk:
                    return
                chk[tuple(arr2)] = 1
                res.append(arr[:])
                return
            
            arr.append(nums[k1])
            dfs(k1+1,arr)
            arr.pop()

            dfs(k1+1, arr)
        dfs(0, [])
        return res
