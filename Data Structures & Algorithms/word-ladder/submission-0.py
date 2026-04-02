class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ref = [beginWord]+wordList
        n = {}
        for i in range(len(ref)):
            if ref[i] not in n:
                n[ref[i]] = []
            for j in range(i+1, len(ref)):
                if ref[j] not in n:
                    n[ref[j]] = []
                c = 0
                for k in range(len(ref[i])):
                    if ref[i][k] != ref[j][k]:
                        c += 1
                if c != 1:
                    continue
                n[ref[i]].append(ref[j])
                n[ref[j]].append(ref[i])
        print(n)

        from collections import deque
        q = deque()
        q.append(beginWord)
        vis = {}
        vis[beginWord] = 0
        while q:
            curr = q.popleft()
            for i in n[curr]:
                if i in vis:
                    continue
                vis[i] = 1+vis[curr]
                q.append(i)
        print(vis)
        return vis.get(endWord, -1)+1
                
        
                