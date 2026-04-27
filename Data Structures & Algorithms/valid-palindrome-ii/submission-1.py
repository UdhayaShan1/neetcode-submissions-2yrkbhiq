class Solution:
    def validPalindrome(self, s: str) -> bool:
        def dfs(i, j, deleted):
            if i >= j:
                return True
            
            if s[i] == s[j]:
                return dfs(i+1, j-1, deleted)
            else:
                if not deleted:
                    return dfs(i+1, j, True) or dfs(i, j-1, True)
                return False
        return dfs(0, len(s)-1, False)
            