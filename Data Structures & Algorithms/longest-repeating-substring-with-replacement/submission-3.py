class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        chk = {}

        def howMany(chk):
            ref = ""
            val = -float('inf')
            for i in chk:
                if chk[i] > val:
                    val = chk[i]
                    ref = i
            count = 0
            for i in chk:
                if i == ref:
                    continue
                count += chk[i]
            return count
        res = 0
        for i in range(len(s)):
            chk[s[i]] = chk.get(s[i], 0)+1
            print(chk, howMany(chk))
            while howMany(chk) > k:
                chk[s[left]] -= 1
                if chk[s[left]] == 0:
                    del chk[s[left]]
                left += 1
            res = max(res, i-left+1)
        return res
            
