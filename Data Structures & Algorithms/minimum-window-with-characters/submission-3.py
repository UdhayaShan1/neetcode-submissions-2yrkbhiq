class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chk_t = {}
        for i in t:
            chk_t[i] = chk_t.get(i, 0)+1

        def valid(chk_t, chk):
            for i in chk_t:
                if i not in chk or chk[i] < chk_t[i]:
                    return False
            return True

        chk = {}
        res = "Z"*2000
        left = 0
        for i in range(len(s)):
            chk[s[i]] = chk.get(s[i], 0)+1
            while True:
                if left < len(s) and s[left] in chk and (s[left] not in chk_t or (chk[s[left]] > chk_t[s[left]])):
                    chk[s[left]] -= 1
                    if chk[s[left]] == 0:
                        del chk[s[left]]
                    left += 1
                else:
                    break
            
            #print(left, i, s[left:i+1])
            if valid(chk_t, chk):
                ref = s[left:i+1]
                if len(ref) < len(res):
                    res = ref
        return res if res != "Z"*2000 else ""

