class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        chk1 = {}
        for i in s1:
            chk1[i] = chk1.get(i, 0)+1
        
        chk2 = {}
        for i in range(len(s1)):
            chk2[s2[i]] = chk2.get(s2[i], 0)+1
        
        left = 0
        right = len(s1)-1
        while True:
            if chk1 == chk2:
                return True

            if right+1 >= len(s2):
                return False
            chk2[s2[left]] -= 1
            if chk2[s2[left]] == 0:
                del chk2[s2[left]]
            chk2[s2[right+1]] = chk2.get(s2[right+1], 0)+1
            left += 1
            right += 1
        
