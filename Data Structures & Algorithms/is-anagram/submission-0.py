class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chk1 = {}
        chk2 = {}
        for i in s:
            chk1[i] = chk1.get(i, 0)+1
        for i in t:
            chk2[i] = chk2.get(i, 0)+1
        return chk1 == chk2