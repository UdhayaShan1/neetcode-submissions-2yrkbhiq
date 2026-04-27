class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        chk = {}
        res = 0
        for i in range(len(s)):
            chk[s[i]] = chk.get(s[i], 0)+1
            while len(chk) > k:
                chk[s[left]] -= 1
                if chk[s[left]] == 0:
                    del chk[s[left]]
                left += 1
            res = max(res, i-left+1)
        return res

