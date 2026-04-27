class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        chk = {}

        def haveDuplicate(chk):
            for i in chk:
                if chk[i] > 1:
                    return True
            return False

        left = 0
        for i in range(len(s)):
            chk[s[i]] = 1+chk.get(s[i], 0)
            while haveDuplicate(chk):
                chk[s[left]] -= 1
                left += 1
            res = max(res, i-left+1)
        return res

