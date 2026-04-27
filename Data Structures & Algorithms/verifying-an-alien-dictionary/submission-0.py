class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos = {}
        for i in range(len(order)):
            pos[order[i]] = i
        
        for i in range(1, len(words)):
            prev = words[i-1]
            curr = words[i]
            min_len = min(len(prev), len(curr))

            can = False
            for j in range(min_len):
                if pos[prev[j]] > pos[curr[j]]:
                    return False
                elif pos[prev[j]] < pos[curr[j]]:
                    can = True
                    break
            if can:
                continue
            
            if len(prev) > len(curr):
                return False
        return True

                

        
