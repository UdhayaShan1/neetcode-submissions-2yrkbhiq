class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        chk = []
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                chk = [i, j]
                break
        if len(chk) == 0:
            return True
        
        ref1 = s[:chk[0]]+s[chk[0]+1:]
        ref2 = s[:chk[1]]+s[chk[1]+1:]
        if ref1 == ref1[::-1] or ref2 == ref2[::-1]:
            return True
        return False
