class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        def replace(chk):
            most = -1
            ref = ""
            for i in chk:
                if chk[i] > most:
                    most = chk[i]
                    ref = i
            count = 0
            for i in chk:
                if i == ref:
                    continue
                count += chk[i]
            return count
        
        res = 0
        chk = {}
        left = 0
        for i in range(len(s)):
            chk[s[i]] = chk.get(s[i], 0)+1
            while replace(chk) > k:
                chk[s[left]] -= 1
                left += 1
            res = max(res, i-left+1)
        return res

        