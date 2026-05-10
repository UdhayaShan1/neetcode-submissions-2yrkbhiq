class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adjList = {}
        for i in accounts:
            for j in range(1, len(i)):
                ref = i[j]
                if ref not in adjList:
                    adjList[ref] = []
                if j+1 < len(i):
                    ref1 = i[j+1]
                    if ref1 not in adjList:
                        adjList[ref1] = []
                    adjList[ref1].append(ref)
                    adjList[ref].append(ref1)
        print(adjList)

        vis = {}
        tag = {}
        def dfs(n, c):
            vis[n] = c
            tag[c].append(n)
            for i in adjList[n]:
                if i in vis:
                    continue
                dfs(i, c)
        
        lol = {}
        for i in accounts:
            if i[1] in vis:
                continue
            name = i[0]
            lol[name] = lol.get(name, 0)+1
            tag1 = (name, lol[name])
            print(tag1)
            tag[tag1] = []

            dfs(i[1], tag1)
        print(tag)
        res = []
        for i in tag:
            res.append([i[0]] + tag[i])
        return res