class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        res = ""
        curr = True
        while i < len(word1) and j < len(word2):
            if curr:
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1
            curr = not curr
        if i < len(word1):
            res += word1[i:]
        if j < len(word2):
            res += word2[j:]
        return res
            
