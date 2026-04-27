class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ref1 = {}
        for i in s1:
            ref1[i] = ref1.get(i, 0)+1

        def possible(chk):
            for i in chk:
                if i not in ref1 or chk[i] > ref1[i]:
                    return False
            return True
        
        def ispermute(chk):
            for i in chk:
                if i not in ref1 or chk[i] != ref1[i]:
                    return False
            for i in ref1:
                if i not in chk or chk[i] != ref1[i]:
                    return False
            return True
        #print(ref1)
        chk = {}
        left = 0
        for i in range(len(s2)):
            chk[s2[i]] = chk.get(s2[i],0)+1
            #print(chk)
            while not possible(chk) and left < i:
                chk[s2[left]] -= 1
                if chk[s2[left]] == 0:
                    del chk[s2[left]]
                left += 1
            if ispermute(chk):
                return True
        return False


                
