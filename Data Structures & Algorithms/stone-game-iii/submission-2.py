class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        sys.setrecursionlimit(999999)
        total = sum(stoneValue)
        from functools import cache
        @cache
        def dfs(alice, k1):
            if k1 >= len(stoneValue):
                return 0
            if alice:
                res = -float('inf')
                curr = 0
                for i in range(1, 4):
                    if k1+i-1 >= len(stoneValue):
                        break
                    curr += stoneValue[k1+i-1]
                    res = max(res, dfs(False, k1+i)+curr)
                return res

            res = float('inf')
            for i in range(1, 4):
                res = min(res, dfs(True, k1+i))
            return res
        res = dfs(True, 0)
        print(res)
        if res > total-res:
            return "Alice" 
        if res < total-res:
            return "Bob"
        return "Tie"
