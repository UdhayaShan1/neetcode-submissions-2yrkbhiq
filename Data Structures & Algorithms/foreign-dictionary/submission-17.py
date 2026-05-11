class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {}
        indeg = {}
        for i in words:
            for j in i:
                adjList[j] = {}
                indeg[j] = 0

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                ref = words[i]
                ref2 = words[j]
                diff = None
                for k in range(min(len(ref), len(ref2))):
                    if ref[k] != ref2[k]:
                        diff = ref[k]
                        if ref2[k] not in adjList[ref[k]]:
                            indeg[ref2[k]] = indeg.get(ref2[k], 0)+1
                        adjList[ref[k]][ref2[k]] = 1

                        break
                if diff is None and len(ref) > len(ref2):
                    return ""
        print(adjList, indeg)

        q = deque()
        for i in indeg:
            if indeg[i] == 0:
                q.append(i)
        
        path = []
        while q:
            curr = q.popleft()
            path.append(curr)
            for i in adjList[curr]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)
        if len(path) != len(adjList):
            return ''
        return ''.join(path)