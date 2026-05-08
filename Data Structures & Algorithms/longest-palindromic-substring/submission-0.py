class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getLongest(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return (i+1, j-1)
        
        res = [0, -1]
        for i in range(len(s)):
            ref = getLongest(i, i)
            if ref[1]-ref[0]+1 > res[1]-res[0]+1:
                res[0] = ref[0]
                res[1] = ref[1]
            if i+1 < len(s) and s[i] == s[i+1]:
                ref = getLongest(i, i+1)

                if ref[1]-ref[0]+1 > res[1]-res[0]+1:
                    res[0] = ref[0]
                    res[1] = ref[1]
        #print(res)
        return s[res[0]:res[1]+1]
        