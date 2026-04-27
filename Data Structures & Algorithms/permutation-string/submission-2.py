class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chk1 = {}
        for i in s1:
            chk1[i] = chk1.get(i, 0)+1
        def isS1(chk1, chk2):
            for i in chk1:
                if i not in chk2:
                    return False
                if chk2[i] < chk1[i]:
                    return False
            for i in chk2:
                if i not in chk1:
                    return False
            return True
        
        left = 0
        right = len(s1)-1
        chk2 = {}
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            chk2[s2[i]] = chk2.get(s2[i], 0)+1
        
        print(chk1, chk2)

        while True:
            if isS1(chk1, chk2):
                return True
            if right+1 >= len(s2):
                break
            chk2[s2[left]] -= 1
            if chk2[s2[left]] == 0:
                del chk2[s2[left]]
            
            chk2[s2[right+1]] = chk2.get(s2[right+1], 0)+1
            left += 1
            right += 1
        return False
        

