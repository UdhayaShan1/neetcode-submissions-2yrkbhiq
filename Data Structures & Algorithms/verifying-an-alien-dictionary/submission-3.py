class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        o = {}
        for i in range(len(order)):
            o[order[i]] = i
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                ref = words[i]
                ref1 = words[j]
                diff = False
                for k in range(min(len(ref), len(ref1))):
                    if ref[k] != ref1[k]:
                        diff = True
                        if o[ref[k]] > o[ref1[k]]:
                            return False
                        break
                if not diff and len(ref) > len(ref1):
                    return False
        return True