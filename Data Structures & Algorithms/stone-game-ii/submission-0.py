class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        from functools import cache
        @cache
        def dfs(a, k1, M):
            if k1 >= len(piles):
                return 0
            if a:
                res = -float('inf')
                
                curr = 0
                for i in range(1, 2*M+1):
                    if k1+i-1 >= len(piles):
                        continue
                    curr += piles[k1+i-1]
                    res = max(res, dfs(not a, k1+i, max(M, i))+curr)
                return res
            res = float('inf')
            
            curr = 0
            for i in range(1, 2*M+1):
                if k1+i-1 >= len(piles):
                    continue
                curr += piles[k1+i-1]
                res = min(res, dfs(not a, k1+i, max(M, i)))
            return res
        return dfs(True, 0, 1)


                    
                    