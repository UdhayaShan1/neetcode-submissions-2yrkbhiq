class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        find = total // 4

        arr = [0]*4
        dp = {}
        def dfs(k1, arr):
            if k1 >= len(matchsticks):
                for i in arr:
                    if i != find:
                        return False
                return True
            key = (k1, tuple(arr))
            if key in dp:
                return dp[key]
            for i in range(len(arr)):
                arr[i] += matchsticks[k1]
                if dfs(k1+1, arr):
                    dp[key] = True
                    return True
                arr[i] -= matchsticks[k1]
            dp[key] = False
            return False
        return dfs(0, arr)
            
