class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        d = {}
        for i in s1:
            d[i] = d.get(i, 0)+1
        left = 0
        right = len(s1)-1
        d2 = {}
        for i in range(left, right+1):
            d2[s2[i]] = d2.get(s2[i], 0)+1
        print(d, d2)
        while True:
            if d == d2:
                return True
            if right+1 >= len(s2):
                return False
            d2[s2[left]] -= 1
            d2[s2[right+1]] = d2.get(s2[right+1], 0)+1
            if d2[s2[left]] == 0:
                del d2[s2[left]]
            left += 1
            right += 1
        

        