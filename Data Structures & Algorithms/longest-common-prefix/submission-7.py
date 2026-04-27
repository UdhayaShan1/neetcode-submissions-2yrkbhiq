class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref = strs[0]
        i = 0
        while i < len(ref):
            done = False
            for j in strs:
                if i >= len(j) or j[i] != ref[i]:
                    #print(j, i)
                    done = True
                    break
            if done:
                break
            i += 1
        return ref[:i]