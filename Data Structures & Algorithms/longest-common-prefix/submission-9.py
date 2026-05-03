class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref = strs[0]
        k1 = 0
        for i in range(len(ref)):
            for j in strs:
                if i >= len(j) or j[i] != ref[i]:
                    return ref[:i]
        return ref 