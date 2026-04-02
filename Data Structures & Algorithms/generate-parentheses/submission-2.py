class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(o, c, r):
            if o == n and c == n:
                res.append(r)
                return
            if o > n or c > n or c > o:
                return
            dfs(o+1, c, r+'(')
            dfs(o, c+1, r+')')
        dfs(0, 0, "")
        return res
