class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ref = {}
        for i in range(len(order)):
            ref[order[i]] = i
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                ref1 = words[i]
                ref2 = words[j]
                diff = ""
                for k in range(min(len(ref1), len(ref2))):
                    if ref1[k] != ref2[k]:
                        diff = ref1[k]
                        if ref[ref1[k]] > ref[ref2[k]]:
                            #print(ref1, ref2, k)
                            return False
                        break
                    
                if not diff and len(ref1) > len(ref2):
                    return False
        return True
