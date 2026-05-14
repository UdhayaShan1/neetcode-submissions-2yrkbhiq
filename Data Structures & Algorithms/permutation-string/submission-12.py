class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        f = Counter(s1)

        s = Counter()
        left = 0
        for i in range(len(s2)):
            s[s2[i]] += 1
            while i-left+1 > len(s1):
                s[s2[left]] -= 1
                if s[s2[left]] == 0:
                    del s[s2[left]]
                left += 1
            if i-left+1 == len(s1):
                if s == f:
                    return True
        return False