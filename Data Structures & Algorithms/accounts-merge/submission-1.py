class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adjList = {}
        for i in accounts:
            name = i[0]
            if i[1] not in adjList:
                adjList[i[1]] = []
            for j in range(2, len(i)):
                prev = i[j-1]
                curr = i[j]
                adjList[prev].append(curr)
                if curr not in adjList:
                    adjList[curr] = []
                adjList[curr].append(prev)
        print(adjList)

        vis = {}
        whose = {}
        def dfs(node, name):
            vis[node] = True
            if name not in whose:
                whose[name] = []
            whose[name].append(node)
            for i in adjList[node]:
                if i in vis:
                    continue
                dfs(i, name)

        ref = {}
        count = 0
        og = {}
        for i in accounts:
            if i[1] in vis:
                continue
            count += 1
            og[count] = i[0]
            dfs(i[1], count)
        #print(whose, og)

        res = []
        for i in whose:
            ref = [og[i]]
            ref.extend(whose[i])
            res.append(ref)
        #print(res)
        return res
            

