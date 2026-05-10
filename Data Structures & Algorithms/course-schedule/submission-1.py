class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        indeg = {}
        for i in range(numCourses):
            adjList[i] = []
            indeg[i] = 0
        for i in prerequisites:
            adjList[i[1]].append(i[0])
            indeg[i[0]] += 1
        
        q = deque()
        for i in indeg:
            if indeg[i] == 0:
                q.append(i)
        
        path = {}
        while q:
            curr = q.popleft()
            path[curr] = 1
            for i in adjList[curr]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)
        return len(path) == numCourses
        