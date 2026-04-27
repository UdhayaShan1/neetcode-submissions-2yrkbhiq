class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        chk2 = {}
        chk1 = {}
        res = float('inf')
        ref1 = ""
        for i in t:
            chk1[i] = chk1.get(i, 0)+1
        #print(chk1)
        def isSub(chk1, chk2):
            for i in chk1:
                if i not in chk2 or chk2[i] < chk1[i]:
                    return False
            return True
            
        for i in range(len(s)):
            ref = s[i]
            chk2[ref] = chk2.get(ref, 0)+1

            if not isSub(chk1, chk2):
                continue
            #print(chk1, chk2, left, i)
            while isSub(chk1, chk2):
                length = i-left+1
                if length < res:
                    res = length
                    ref1 = s[left:i+1]
                chk3 = chk2.copy()
                chk3[s[left]] -= 1
                if chk3[s[left]] == 0:
                    del chk3[s[left]]
                if not isSub(chk1, chk3):
                    break
                chk2 = chk3
                left += 1
        return ref1




