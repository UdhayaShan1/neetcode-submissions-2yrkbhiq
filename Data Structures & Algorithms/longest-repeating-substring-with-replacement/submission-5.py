class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def count(chk):
            most = -float('inf')
            most_r = ""
            count = 0
            for i in chk:
                count += chk[i]
                if chk[i] > most:
                    most = chk[i]
                    most_r = i
            return count-most
        
        left = 0
        c = {}
        res = 0
        for i in range(len(s)):
            c[s[i]] = c.get(s[i], 0)+1
            while count(c) > k:
                #print(s, left)
                c[s[left]] -= 1
                if c[s[left]] == 0:
                    del c[s[left]]
                left += 1
            res = max(res, i-left+1)
        return res

            