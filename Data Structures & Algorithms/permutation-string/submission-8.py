class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        ref1 = {}
        for i in s1:
            ref1[i] = ref1.get(i, 0)+1
        ref2 = {}
        for i in range(len(s1)):
            ref2[s2[i]] = ref2.get(s2[i], 0)+1
        
        left = 0
        right = len(s1)-1
        while True:
            if ref1 == ref2:
                return True
            if right+1 >= len(s2):
                return False
            ref2[s2[left]] -= 1
            if ref2[s2[left]] == 0:
                del ref2[s2[left]]
            ref2[s2[right+1]] = ref2.get(s2[right+1], 0)+1
            left += 1
            right += 1
            
            
        