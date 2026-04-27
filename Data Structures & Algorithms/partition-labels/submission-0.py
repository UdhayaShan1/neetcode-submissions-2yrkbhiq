class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = {}
        for i in range(len(s)):
            pos[s[i]] = i
        
        i = 0
        res = []
        #print(pos)
        find = 0
        while i < len(s):
            length = 0
            while True:
                ref = s[i]
                find = max(find, pos[ref])
                length += 1
                i += 1
                #print('@', ref, find, length, i)
                if i > find:
                    break

            res.append(length)
        return res
