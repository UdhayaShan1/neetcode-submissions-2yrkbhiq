class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {}
        indeg = {}
        s = set()
        for i in words:
            for j in i:
                s.add(j)

        for i in s:
            adjList[i] = {}
            indeg[i] = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                ref = words[i]
                ref2 = words[j]
                find = ref if len(ref) < len(ref2) else ref2
                l1 = None
                l2 = None
                for k in range(len(find)):
                    if ref[k] != ref2[k]:
                        l1 = ref[k]
                        l2 = ref2[k]
                        break
                #print(ref, ref2, l1, l2)
                if l1:
                    if l2 not in adjList[l1]:
                        indeg[l2] += 1
                    adjList[l1][l2] = 1
                else:
                    if len(ref) > len(ref2):
                        return ""

        #print(adjList, indeg)

        from collections import deque
        q = deque()
        for i in indeg:
            if indeg[i] == 0 :
                q.append(i)
        path = []
        while q:
            curr = q.popleft()
            path.append(curr)
            for i in adjList[curr]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)
        if len(path) < len(s):
            return ""
        return ''.join(path)
                    