class Solution:
    def minWindow(self, s: str, t: str) -> str:


        chk_t = {}
        for i in t:
            chk_t[i] = chk_t.get(i, 0)+1
        #print(chk_t)

        def valid(chk):
            for i in chk_t:
                if i not in chk or chk[i] < chk_t[i]:
                    return False
            return True
                    
        def canRemove(chk, ref):
            return ref not in chk_t or chk[ref] > chk_t[ref]

        left = 0
        chk = {}
        res = None
        res_m = float('inf')
        for i in range(len(s)):
            #print(i, s[i], chk)
            chk[s[i]] = chk.get(s[i], 0)+1
            print(i, s[i], chk, chk_t)
            while left <= i and canRemove(chk, s[left]):
                #print(left, chk)
                chk[s[left]] -= 1
                if chk[s[left]] == 0:
                    del chk[s[left]]
                left += 1
            #print(left, i, chk)
            l = i-left+1
            if valid(chk) and l < res_m:
                #print(chk, left, i)
                res_m = l
                res = (left, i)
        return s[res[0]:res[1]+1] if res else ""




