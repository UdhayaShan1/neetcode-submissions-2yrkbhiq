class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        sys.setrecursionlimit(99999999)
        parent = {}
        dp = {}
        def dfs(k1, prev):
            if k1 >= len(nums):
                return 0
            key = (k1, prev)
            if key in dp:
                return dp[key]
            if prev == -1:
                best = 0
                res1 = dfs(k1+1, k1)+1
                if res1 > best:
                    best = res1
                    parent[key] = (k1+1, k1)
                res2 = dfs(k1+1, prev)
                if res2 > best:
                    best = res2
                    parent[key] = (k1+1, prev)
            else:
                best = 0
                if nums[k1] % nums[prev] == 0:
                    res1 = dfs(k1+1, k1)+1
                    if res1 > best:
                        best = res1
                        parent[key] = (k1+1, k1)
                res2 = dfs(k1+1, prev)
                if res2 > best:
                    best = res2
                    parent[key] = (k1+1, prev)
            dp[key] = best
            return dp[key]
        dfs(0, -1)
        #print(parent)

        start = (0, -1)
        res = []
        while start in parent:
            tmp = parent[start]
            if tmp[1] == start[0]:
                res.append(nums[start[0]])
            start = tmp
        return res