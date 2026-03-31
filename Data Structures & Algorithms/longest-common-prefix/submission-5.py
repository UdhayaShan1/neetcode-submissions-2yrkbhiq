class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pos = -1
        for i in range(len(strs[0])):
            bad = False
            ref = strs[0][i]
            for j in strs:
                if i >= len(j) or j[i] != ref:
                    bad = True
                    break
            if bad:
                break
            pos = i
        #print(pos)
        return strs[0][:pos+1]
