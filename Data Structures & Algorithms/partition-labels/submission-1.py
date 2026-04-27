class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = {}
        for i in range(len(s)):
            pos[s[i]] = i
        
        res = []
        i = 0
        while i < len(s):
            find = pos[s[i]]
            start = i
            while i < len(s):
                find = max(find, pos[s[i]])
                if i == find:
                    break
                i += 1
            res.append(i-start+1)
            i += 1
        return res
            

