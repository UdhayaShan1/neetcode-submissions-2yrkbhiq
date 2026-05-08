class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        from functools import cache
        @cache
        def dfs(i, j):
            if i >= len(s1) and j >= len(s2):
                return True
            
            if i >= len(s1):
                if s2[j] != s3[i+j]:
                    return False
                return dfs(i, j+1)
            if j >= len(s2):
                if s1[i] != s3[i+j]:
                    return False
                return dfs(i+1, j)
            l = i+j
            
            if s1[i] != s3[l] and s2[j] != s3[l]:
                return False

            if s1[i] == s3[l]:
                if dfs(i+1, j):
                    return True
            if s2[j] == s3[l]:
                if dfs(i, j+1):
                    return True
            return False
        return dfs(0, 0)
            
                
