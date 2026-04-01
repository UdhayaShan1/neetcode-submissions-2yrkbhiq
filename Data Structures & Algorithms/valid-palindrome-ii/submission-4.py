class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid(i, j):
            print(i, j)
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            return valid(i+1, j-1)
        
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                x = valid(i+1, j) 
                y = valid(i, j-1)
                if x or y:
                    return True
                return False
            i += 1
            j -= 1
        return True

            