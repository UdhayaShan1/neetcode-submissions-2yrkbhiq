class Solution:
    def isPalindrome(self, s: str) -> bool:
        char = "abcdefghijklmnopqrstuvwxyz0123456789"
        i = 0
        j = len(s)-1
        while i < j:
            if s[i].lower() not in char:
                i += 1
                continue
            if s[j].lower() not in char:
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True