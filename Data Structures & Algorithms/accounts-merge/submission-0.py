class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adjList = {}
        for i in accounts:
            name = i[0]
            for j in range(2, len(i)):
                prev = i[j-1]
                curr = i[j]
                if prev not in adjList:
                    adjList[prev] = []
                if curr not in adjList:
                    adjList[curr] = []
                adjList[prev].append(curr)
                adjList[curr].append(prev)
        print(adjList)

        taken = {}
        vis = {}
        name_lst = {}
        def dfs(node, name):
            vis[node] = name
            if name not in name_lst:
                name_lst[name] = {}
            name_lst[name][node] = 1
            
            for i in adjList.get(node, []):
                if i in vis:
                    continue
                dfs(i, name)
        
        for i in accounts:
            name = i[0]
            if i[1] in vis:
                continue
            taken[name] = taken.get(name, 0)+1
            dfs(i[1], f"{name}{taken[name]}")
        print(name_lst)


        def get_name(ref):
            r = []
            for i in ref:
                if '1' <= i <= '9':
                    break
                r.append(i)
            return ''.join(r)

        res = []
        for i in name_lst:
            r = get_name(i)
            res.append([r] + list(name_lst[i].keys()))
        return res
            
                
                