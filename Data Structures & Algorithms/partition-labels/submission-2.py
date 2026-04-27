class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = {}
        for i in range(len(s)):
            pos[s[i]] = i
        
        i = 0
        res = []
        while i < len(s):
            ref = s[i]
            find = pos[ref]
            count = 1
            while True:
                find = max(find, pos[s[i]])
                if i == find:
                    break
                i += 1
                count += 1
            res.append(count)
            i = max(i, i+1)
        return res
                




