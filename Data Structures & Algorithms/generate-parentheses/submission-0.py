class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(o, length, str1):
            if length == n*2:
                if o == 0:
                    res.append(str1)
                return
            if o < n:
                dfs(o+1, length+1, str1+"(")
            if o > 0:
                dfs(o-1, length+1, str1+")")


        dfs(0, 0, '')
        return res