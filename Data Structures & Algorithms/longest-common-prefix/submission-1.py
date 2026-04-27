class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        chk = {}
        for i in strs:
            ref = ""
            for j in i:
                ref += j
                chk[ref] = chk.get(ref, 0)+1
        hmm = 0
        res = ""
        for i in chk:
            if chk[i] == len(strs) and len(i) > hmm:
                hmm = len(i)
                res = i
        return res
