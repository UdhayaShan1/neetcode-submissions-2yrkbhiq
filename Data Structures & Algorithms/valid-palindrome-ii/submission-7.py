class Solution:
    def validPalindrome(self, s: str) -> bool:
        from functools import cache
        @cache
        def valid(i, j):
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            return valid(i+1, j-1)
        
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                if valid(i+1, j) or valid(i, j-1):
                    return True
                return False
            i += 1
            j -= 1
        return True
            