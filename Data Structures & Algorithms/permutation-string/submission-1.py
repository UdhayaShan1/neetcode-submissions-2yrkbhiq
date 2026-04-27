class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def notSub(chk1, chk2):
            for i in chk2:
                if i not in chk1 or chk2[i] > chk1[i]:
                    return True
        def isSub(chk1, chk2):
            for i in chk1:
                if i not in chk2 or chk2[i] != chk1[i]:
                    return False
            return True


        chk1 = {}
        for i in s1:
            chk1[i] = chk1.get(i, 0)+1
        
        left = 0
        chk2 = {}
        for i in range(len(s2)):
            ref = s2[i]
            chk2[ref] = chk2.get(ref, 0)+1
            while notSub(chk1, chk2):
                chk2[s2[left]] -= 1
                if chk2[s2[left]] == 0:
                    del chk2[s2[left]]
                left += 1
            if isSub(chk1, chk2):
                return True
        return False
            
            

