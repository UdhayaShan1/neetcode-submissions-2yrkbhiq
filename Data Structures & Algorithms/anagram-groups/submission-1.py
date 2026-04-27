class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new = {}
        for i in strs:
            lst = list(i)
            lst.sort()
            ref = ''.join(lst)
            if ref not in new:
                new[ref] = []
            new[ref].append(i)
        return(list(new.values()))