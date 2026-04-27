class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def invalid(chk):
            ref = ""
            max1 = -float('inf')
            for i in chk:
                if chk[i] > max1:
                    max1 = chk[i]
                    ref = i

            count = 0
            for i in chk:
                if i == ref or chk[i] == 0:
                    continue
                count += chk[i]
            return False if count <= k else True
        
        res = -float('inf')
        chk = {}
        left = 0
        for i in range(len(s)):
            if s[i] not in chk:
                chk[s[i]] = 0
            chk[s[i]] += 1
            #print(chk)
            while invalid(chk):
                chk[s[left]] -= 1
                left += 1
            res = max(res, i-left+1)
        return res


