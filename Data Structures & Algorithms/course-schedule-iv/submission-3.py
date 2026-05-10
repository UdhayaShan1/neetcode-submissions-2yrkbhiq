class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = {}
        indeg = {}
        for i in range(numCourses):
            adjList[i] = []
            indeg[i] = 0
        for i in prerequisites:
            adjList[i[0]].append(i[1])
        

        from functools import cache

        @cache
        def dfs(n, dst):
            if n == dst:
                return True
            
            for i in adjList[n]:
                if dfs(i, dst):
                    return True
            return False
        res = []
        for i in queries:
            res.append(dfs(i[0], i[1]))
        return res

        
        