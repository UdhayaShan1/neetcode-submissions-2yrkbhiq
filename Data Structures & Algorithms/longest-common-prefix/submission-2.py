class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        chk = {}
        for i in strs:
            ref = ""
            for j in i:
                ref += j
                chk[ref] = chk.get(ref, 0)+1
        res = ""
        #print(chk)
        for i in chk:
            if chk[i] != len(strs):
                continue
            if len(i) > len(res):
                res = i
        return res