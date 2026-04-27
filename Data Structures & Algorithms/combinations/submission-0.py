class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(arr):
            if len(arr) == k:
                res.append(arr[:])
                return
            
            prev = 0 if len(arr) == 0 else arr[-1]
            for i in range(prev+1, n+1):
                arr.append(i)
                dfs(arr)
                arr.pop()
        dfs([])
        return res