class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        tmp = [beginWord]+wordList+[endWord]
        adjList = {}
        for i in range(len(tmp)):
            for j in range(i+1, len(tmp)):
                ref = tmp[i]
                ref1 = tmp[j]
                if ref not in adjList:
                    adjList[ref] = []
                if ref1 not in adjList:
                    adjList[ref1] = []
                c = 0
                for j in range(len(ref)):
                    if ref[j] != ref1[j]:
                        c += 1
                if c == 1:
                    adjList[ref].append(ref1)
                    adjList[ref1].append(ref)
        #print(adjList)
        if endWord not in wordList:
            return 0
        
        q = deque()
        d = {beginWord:0}
        q.append(beginWord)
        while q:
            curr = q.popleft()
            for i in adjList[curr]:
                if i in d:
                    continue
                d[i] = 1+d[curr]
                q.append(i)
        return d.get(endWord, -1)+1