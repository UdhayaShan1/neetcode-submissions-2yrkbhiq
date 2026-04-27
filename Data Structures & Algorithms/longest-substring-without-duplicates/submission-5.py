class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        chk = {}
        def bad(chk):
            for i in chk:
                if chk[i] > 1:
                    return True
            return False

        res = 0
        for i in range(len(s)):
            chk[s[i]] = chk.get(s[i], 0)+1
            #print(i, chk)
            while bad(chk):
                chk[s[left]] -= 1
                if chk[s[left]] == 0:
                    del chk[s[left]]
                left += 1
            res = max(res, i-left+1)
        return res
            

