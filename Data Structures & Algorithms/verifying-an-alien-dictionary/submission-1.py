class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        o = {}
        for i in range(len(order)):
            o[order[i]] = i
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                ref = words[i]
                ref2 = words[j]
                diff = None
                for k in range(min(len(ref), len(ref2))):
                    if ref[k] != ref2[k]:
                        diff = ref[k]
                        if o[ref[k]] > o[ref2[k]]:
                            return False
                        break
                if diff is None and len(ref) > len(ref2):
                    return False

        return True