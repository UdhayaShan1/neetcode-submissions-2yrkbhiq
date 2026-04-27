class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def findRepl(chk):
            most = 0
            r = ''
            for i in chk:
                if chk[i] > most:
                    most = chk[i]
                    r = i
            count = 0
            for i in chk:
                if i == r:
                    continue
                count += chk[i]
            return count
        
        left = 0
        chk = {}
        res = 0
        for i in range(len(s)):
            chk[s[i]] = chk.get(s[i], 0)+1

            while findRepl(chk) > k:
                chk[s[left]] -= 1
                if chk[s[left]] == 0:
                    del chk[s[left]]
                left += 1
            
            res = max(res, i-left+1)
        return res