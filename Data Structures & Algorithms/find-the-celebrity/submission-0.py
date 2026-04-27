# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        indeg = {}
        outdeg = {}
        for i in range(n):
            if i not in outdeg:
                outdeg[i] = 0
            for j in range(n):
                if j not in indeg:
                    indeg[j] = 0
                if i == j:
                    continue
                if knows(i, j):
                    indeg[j] += 1
                    outdeg[i] += 1
        #print(indeg, outdeg)

        for i in range(n):
            if indeg[i] == n-1 and outdeg[i] == 0:
                return i
        return -1
                
        