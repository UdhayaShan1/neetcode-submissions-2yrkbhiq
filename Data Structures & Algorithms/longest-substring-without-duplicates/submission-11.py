class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ref = {}
        left = 0
        res = 0
        for i in range(len(s)):
            ref[s[i]] = ref.get(s[i], 0)+1
            while ref[s[i]] > 1:
                ref[s[left]] -= 1
                if ref[s[left]] == 0:
                    del ref[s[left]]
                left += 1
            res = max(res, i-left+1)
        return res