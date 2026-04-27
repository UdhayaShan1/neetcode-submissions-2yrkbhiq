class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(k1, arr):
            if len(arr) == k:
                res.append(arr[:])
                return
            if k1 > n:
                return
            
            dfs(k1+1, arr+[k1])
            dfs(k1+1, arr)
        dfs(1, [])
        return res