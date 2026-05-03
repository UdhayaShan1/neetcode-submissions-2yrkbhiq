class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        d = {}
        res = 0
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0)+1
            while d.get(s[i], 0) > 1:
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    del d[s[left]]
                left += 1
            res = max(res, i-left+1)
        return res