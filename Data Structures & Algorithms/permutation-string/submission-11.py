class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        c = Counter(s1)
        c2 = Counter()
        left = 0
        for i in range(len(s2)):
            c2[s2[i]] += 1
            while i-left+1 > len(s1):
                c2[s2[left]] -= 1
                if c2[s2[left]] == 0:
                    del c2[s2[left]]
                left += 1
            if i-left+1 == len(s1):
                if c2 == c:
                    return True
        return False
