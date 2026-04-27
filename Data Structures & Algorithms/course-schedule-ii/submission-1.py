class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = {}
        adjList = {}
        for i in range(numCourses):
            indeg[i] = 0
            adjList[i] = []
        
        from queue import Queue
        for i in prerequisites:
            adjList[i[1]].append(i[0])
            indeg[i[0]] += 1
        
        q = Queue()
        for i in indeg:
            if indeg[i] == 0:
                q.put(i)
        
        res = []
        while not q.empty():
            curr = q.get()
            res.append(curr)
            for i in adjList[curr]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.put(i)
        return res if len(res) == numCourses else []

    