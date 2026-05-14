class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        #print(q, adjList)
        path = []
        while q:
            curr = q.popleft()
            path.append(curr)
            for i in adjList[curr]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)
        if len(path) != numCourses:
            return []
        return path
