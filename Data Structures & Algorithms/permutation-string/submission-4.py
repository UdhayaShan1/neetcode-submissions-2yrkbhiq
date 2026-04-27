class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        chk = {}
        ref = {}
  
        for i in range(len(s1)):
            ref[s1[i]] = ref.get(s1[i], 0)+1
            chk[s2[i]] = chk.get(s2[i], 0)+1
        #print(chk)

        
        def valid(chk):
            for i in chk:
                if i not in ref:
                    return False
                if chk[i] < ref[i]:
                    return False
            for i in ref:
                if i not in chk or chk[i] < ref[i]:
                    return False
            return True
        left = 0
        right = len(s1)-1

        while right < len(s2):
            print(chk)
            if valid(chk):
                return True
            if right+1 >= len(s2):
                break
            chk[s2[left]] -= 1
            chk[s2[right+1]] = chk.get(s2[right+1], 0)+1
            if chk[s2[left]] == 0:
                del chk[s2[left]]
            left += 1
            right += 1
        return False
        
         