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
                ref1 = words[j]
                diff = False
                for k in range(min(len(ref), len(ref1))):
                    if ref[k] != ref1[k]:
                        diff = True
                        if ref1[k] not in adjList[ref[k]]:
                            indeg[ref1[k]] += 1
                        adjList[ref[k]][ref1[k]] = 1
                        break
                if not diff and len(ref) > len(ref1):
                    return ""
        #print(adjList, indeg)

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
        #print(path)
        if len(path) != len(adjList):
            return ""
        return ''.join(path)

                
