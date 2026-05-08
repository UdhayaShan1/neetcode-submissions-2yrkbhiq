class Solution:
    def countSubstrings(self, s: str) -> int:
        def getLongest(i, j):
            res = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                res += 1
                i -= 1
                j += 1
            return res
        
        res = 0
        for i in range(len(s)):
            res += getLongest(i, i)
            if i+1 < len(s) and s[i] == s[i+1]:
                res += getLongest(i, i+1)
        #print(res)
        return res