class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []
        for i in prerequisites:
            adjList[i[0]].append(i[1])
        dp = {}
        def dfs(node, dst):
            if node == dst:
                return True
            if len(adjList.get(node, [])) == 0:
                return False
            key = (node, dst)
            if key in dp:
                return dp[key]
            for i in adjList[node]:
                if dfs(i, dst):
                    dp[key] = True
                    return True
            dp[key] = False
            return False
        res = []
        for i in queries:
            res.append(dfs(i[0], i[1]))
        return res

            

            