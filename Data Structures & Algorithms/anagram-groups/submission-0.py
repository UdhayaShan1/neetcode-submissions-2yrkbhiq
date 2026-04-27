class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            ref = []
            for j in i:
                ref.append(j)
            ref.sort()
            ref = ''.join(ref)
            
            if ref not in res:
                res[ref] = []
            res[ref].append(i)

        return list(res.values())

        