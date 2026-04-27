class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid(s):
            i = 0
            j = len(s)-1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        i = 0
        j = len(s)-1
        pos = False
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                pos = True
                #print(i, j)
                v1 = valid(s[i+1:j+1])
                v2 = valid(s[i:j])
                #print(s[i+1:], s[:j])
                if v1 or v2:
                    return True
                return False
        return True
