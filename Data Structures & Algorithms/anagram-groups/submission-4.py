class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chk = {}
        for i in strs:
            ref = list(i)
            ref.sort()
            ref = ''.join(ref)
            if ref not in chk:
                chk[ref] = []
            chk[ref].append(i)
        #print(chk)
        res = []
        for i in chk:
            res.append(chk[i])
        return res
