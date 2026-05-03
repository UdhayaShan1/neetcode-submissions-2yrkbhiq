class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = {}
        for i in s1:
            d1[i] = d1.get(i, 0)+1
        d2 = {}
        left = 0
        for i in range(len(s2)):
            d2[s2[i]] = d2.get(s2[i], 0)+1
            while i-left+1 > len(s1):
                d2[s2[left]] -= 1
                if d2[s2[left]] == 0:
                    del d2[s2[left]]
                left += 1
            if i-left+1 == len(s1):
                if d1 == d2:
                    return True
        return False