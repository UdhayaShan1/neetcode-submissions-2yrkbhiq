class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref = {}
        for i in strs:
            hmm = []
            for j in i:
                hmm.append(j)
            hmm.sort()
            hmm = ''.join(hmm)
            if hmm not in ref:
                ref[hmm] = [i]
            else:
                ref[hmm].append(i)
        return list(ref.values())