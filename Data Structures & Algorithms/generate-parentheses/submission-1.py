class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(f, s, str1):
            if f == n and s == n:
                res.append(str1)
                return
            if f > n or s > n:
                return
            if s > f:
                return n


            dfs(f+1,s, str1+"(")
            dfs(f,s+1, str1+")")
        dfs(0, 0, "")
        return res
