class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chk = {}
        for i in strs:
            ref = {}
            quick = {}
            for j in i :
                quick[j] = quick.get(j, 0)+1
            for j in "abcdefghijklmnopqrstuvwxyz":
                ref[j] = quick.get(j, 0)
            
            hmm = tuple([tuple(ref), tuple(ref.values())])
            print(i, hmm)
            if hmm not in chk:
                chk[hmm] = []
            if hmm in chk:
                chk[hmm].append(i)
        return list(chk.values())
